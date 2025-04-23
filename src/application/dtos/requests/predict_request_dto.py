from pydantic import BaseModel

class PredictRequestDto(BaseModel):
    text: str
