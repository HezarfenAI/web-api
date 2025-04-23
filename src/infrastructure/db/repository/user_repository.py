from db.repository.base import BaseRepository
from domain.common.user import User

class UserRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, User)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()
