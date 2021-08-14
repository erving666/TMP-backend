from sqlalchemy import Column
from sqlalchemy.types import String, Integer
from app.models import BaseModel


class User(BaseModel):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))

    def to_json(self):
        return {
            'id': self.id,
            'login_id': self.username,
            'password': self.password
        }

    def to_token_json(self):
        return {
            'id': self.id,
            'username': self.username
        }
