from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from datetime import datetime
from .base import Base

class TrainDataset(Base):
    __tablename__ = 'train_dataset'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    label = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
