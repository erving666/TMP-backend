class BaseRepository(object):
    pass


class FSQLALchemyRepository(BaseRepository):
    def __init__(self, model, session):
        self.model = model
        self.session = session
