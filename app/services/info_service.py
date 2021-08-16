import inject
from app.repositorys.info_repository import InfoRepository


class InfoService:
    info_repository = inject.attr(InfoRepository)

    def info_persist(self, entity):  
        self.info_repository.info_persist(entity=entity)


