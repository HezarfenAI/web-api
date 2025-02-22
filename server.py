import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from hezarfen_ai.model import ModelLoader

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tüm kaynaklara izin verir
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP metodlarına izin verir (GET, POST, PUT, DELETE vs.)
    allow_headers=["*"],  # Tüm header'lara izin verir
)

model_loader = ModelLoader()

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
