from fastapi import APIRouter
from fastapi.params import Depends, Security
from fastapi.security import HTTPBearer
from application.dtos.requests.auth.login_request_dto import LoginRequestDto
from application.dtos.requests.register_request_dto import RegisterRequestDto
from application.services.auth_services import AuthService
from infrastructure.db.database import SessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])
session = SessionLocal()
auth_services = AuthService(session)
security = HTTPBearer()

@router.post("/register")
async def register_user(request: RegisterRequestDto):
    response = auth_services.register(request)

    return { "status": response }

@router.post("/login")
async def login_user(request: LoginRequestDto):
    access_token = auth_services.login(request.email, request.password)

    return { "access_token": access_token }

@router.get("/test")
async def test(credentials = Security(security), current_user = Depends(auth_services.get_current_user)):
    return { "message": "Hello World!" }
