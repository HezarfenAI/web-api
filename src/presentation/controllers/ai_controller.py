from fastapi import APIRouter
from application.dtos.requests.add_data_dto import AddDataRequestDto
from application.dtos.requests.predict_request_dto import PredictRequestDto
from application.services.ai_services import AIServices

router = APIRouter(prefix="/ai", tags=["AI"])
ai_services = AIServices()

@router.post("/predict")
def predict(data: PredictRequestDto):
    result = ai_services.predict(data.text)

    return { "is_success": True, "analyze_result": result }

@router.post("/train")
def train(data: AddDataRequestDto):
    ai_services.train(data)

    return { "is_success": True }
