import os
import sys
import pandas as pd
import csv

from pydantic import BaseModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from hezarfen_ai.model import ModelLoader
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tüm kaynaklara izin verir
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP metodlarına izin verir (GET, POST, PUT, DELETE vs.)
    allow_headers=["*"],  # Tüm header'lara izin verir
)

model_loader = ModelLoader(csv_file="./turkish_news.csv", model_file="./hezarfen.pkl", dataset_file="./turkish_news.csv")
model_loader.run_model()

class AddDataModel(BaseModel):
    text: str
    label: str
    url: str

@app.post("/v1/hezarfen/fake-news-checker")
async def read_root(text: str):
    try:
        result = model_loader.ask(text)

        return { "is_success": True, "analyze_result": "Gerçek" if result[0] == "TRUE" else "Sahte" }

    except Exception as e:
        return {
            "error": str(e),
            "is_success": False
        }

@app.post("/v1/hezarfen/teach")
async def add_data(request: AddDataModel):

    if os.path.exists('./datasets/generated_dataset.csv') is not True:
        with open('./datasets/generated_dataset.csv', 'w') as file:
            fieldnames = ['text', 'label', 'url']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    df = pd.read_csv('./datasets/generated_dataset.csv')

    with open('./datasets/generated_dataset.csv', 'a', newline='') as csvfile:
        fieldnames = ['text', 'label', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            "text": request.text,
            "label": request.label,
            "url": request.url
        })

    return { "is_success": True }