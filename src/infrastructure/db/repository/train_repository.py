from .base import BaseRepository
from domain.common.train_dataset import TrainDataset

class TrainRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, TrainDataset)
