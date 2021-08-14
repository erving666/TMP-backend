class BaseRepository(object):
    def get(self, **pk):
        raise NotImplementedError

    def get2(self, **pk):
        raise NotImplementedError

    def find(self, **key):
        raise NotImplementedError

    def find2(self, **key):
        raise NotImplementedError

    def delete(self, entity):
        raise NotImplementedError

    def all(self):
        raise NotImplementedError

    def persist(self, entity):
        raise NotImplementedError


class FSQLALchemyRepository(BaseRepository):
    def __init__(self, model, session):
        self.model = model
        self.session = session

    def get(self, **pk):
        return self.session.query(self.model).filter_by(**pk).one()

    def get2(self, **pk):
        return self.session.query(self.model).filter(**pk).one()

    def find(self, **key):
        return self.session.query(self.model).filter_by(**key).all()

    def find2(self, **key):
        return self.session.query(self.model).filter(*key).all()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()

    def all(self):
        return list(self.session.query(self.model).all())

    def persist(self, entity):
        self.session.add(entity)
        self.session.commit()


