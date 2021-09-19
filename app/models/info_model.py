from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer
from app.models import BaseModel
from app.models import User


class Info(BaseModel):
    __tablename__ = "Info"
    # __table_args__ = {"schema": "hnsd"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    phone = Column(String(100))

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'phone': self.phone
        }

    def to_token_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }
