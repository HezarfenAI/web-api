from sqlalchemy import Column, Integer, String, DateTime, Boolean
import datetime
from .base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=lambda: datetime.datetime.utcnow(), onupdate=lambda: datetime.datetime.utcnow())
    deleted_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
