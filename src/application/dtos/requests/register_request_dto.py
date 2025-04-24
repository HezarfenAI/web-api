from pydantic import BaseModel

class RegisterRequestDto(BaseModel):
    id: str
    email: str
    password: str
    name: str
