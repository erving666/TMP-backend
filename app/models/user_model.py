from sqlalchemy import Column
from sqlalchemy.types import String
from app.models import BaseModel


class User(BaseModel):
    __tablename__ = "User"
    id = Column(String(100), primary_key=True)
    username = Column(String(100))
    password = Column(String(100))
