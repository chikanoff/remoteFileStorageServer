from enum import unique
from flask_restx.utils import default_id
from conduit.database import Column, String, Model


class User(Model):
    __tablename__ = "users"
    username = Column(String(64), nullable=False, unique=True)
    passwrod = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    role = Column(String(32), default="user", nullable=False)

    def __repr__(self) -> str:
        return self.username
