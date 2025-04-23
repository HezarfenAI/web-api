from hezarfenai.models.model_loader import ModelLoader
from infrastructure.db.database import SessionLocal
from domain.common.train_dataset import TrainDataset
from infrastructure.db.repository.train_repository import TrainRepository
from application.dtos.requests.add_data_dto import AddDataRequestDto

class AIServices:
    def __init__(self,):
        self.session = SessionLocal()
        self.model_loader = ModelLoader(
            model_path="outputs/hezarfen.pkg",
            dataset_file="datasets/turkish_news.csv",
            model_type="hezarfenai",
            model_generation=False
        )


    def train(self, request: AddDataRequestDto):
        session = SessionLocal()
        train_repository = TrainRepository(session)

        model = TrainDataset(text=request.text, label=request.label, url=request.url)
        train_repository.add(model)

        session.close()

    def predict(self, text: str):
        return self.model_loader.ask(text)
