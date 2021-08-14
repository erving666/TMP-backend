from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

dbmetadata = MetaData()
BaseModel = declarative_base(metadata=dbmetadata)

from .user_model import User