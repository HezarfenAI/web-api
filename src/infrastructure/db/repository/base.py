class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, id):
        return self.session.query(self.model).filter(self.model.id == id).first()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()
