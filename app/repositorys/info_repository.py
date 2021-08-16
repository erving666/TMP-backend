from db import InfoSQL


class InfoRepository:
    
    def info_persist(self, entity):
        InfoSQL.persist(entity=entity)

