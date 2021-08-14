from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.repositorys import FSQLALchemyRepository
from config import Config
from app.models import User, dbmetadata

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
DBSession = sessionmaker(bind=engine)
session = DBSession()
UserSQL = FSQLALchemyRepository(User, session)


def init_db():
    dbmetadata.create_all(bind=engine)
