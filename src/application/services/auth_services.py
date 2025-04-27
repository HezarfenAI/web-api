from dotenv.main import load_dotenv
from fastapi import Depends
from application.dtos.requests.register_request_dto import RegisterRequestDto
from domain.common.user import User
from infrastructure.db.repository.user_repository import UserRepository
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from fastapi.security import OAuth2PasswordBearer
import os
from fastapi import status, HTTPException
from jwt.exceptions import PyJWTError

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 1

class AuthService:
    def __init__(self, session):
        self.session = session
        self.user_repository = UserRepository(self.session)

    def _verify_password(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    def _encrypt_password(self, password: str):
        return pwd_context.hash(password)

    def register(self, request: RegisterRequestDto):
        model = User(
            email=request.email,
            password=self._encrypt_password(request.password),
            name=request.name
        )
        self.user_repository.add(model)

        return True

    def get_current_user(self, token: str = Depends(oauth2_scheme)):
        print("BEN ÇALIŞTIM ", token)
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            print("payload ", payload)
            user_id = payload.get("sub")
            if user_id is None:
                raise credentials_exception
        except Exception as e:
            print(f"JWT Error: {type(e).__name__}, {str(e)}")  # Spesifik hata mesajını yazdırır
            raise credentials_exception

        user = self.user_repository.get_by_id(int(user_id))
        if user is None:
            raise credentials_exception
        return user

    def login(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)

        if user and self._verify_password(password, user.password):
            return self._create_access_token({"sub": str(user.id)})

        return False

    def _create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encoded_jwt
