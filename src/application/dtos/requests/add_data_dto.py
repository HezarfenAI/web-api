from pydantic import BaseModel

class AddDataRequestDto(BaseModel):
    text: str
    label: str
    url: str
