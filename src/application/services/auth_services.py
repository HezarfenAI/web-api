from application.dtos.requests.register_request_dto import RegisterRequestDto
from domain.common.user import User
from src.infrastructure.db.repository.user_repository import UserRepository

class AuthService:
    def __init__(self, session):
        self.session = session
        self.user_repository = UserRepository(self.session)

    def register(self, request: RegisterRequestDto):
        password = None
        model = User(email=request.email, password=password, name=request.name)
        self.user_repository.add(model)
        pass

    def login(self, email: str, password: str):
        # Implement login logic here
        pass

    def encrypt_password(self, password: str):
        pass

    def decrypt_password(self, encrypted_password: str):
        # Implement password decryption logic here
        pass
