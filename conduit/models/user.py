from enum import unique
from flask_restx.utils import default_id
from conduit.database import Column, String, Model
from werkzeug.security import generate_password_hash, check_password_hash


class User(Model):
    __tablename__ = "users"
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    role = Column(String(32), default="user", nullable=False)

    def __repr__(self) -> str:
        return self.username

    @classmethod
    def create(cls, first_name, last_name, email, username, password, role="user"):
        password_hash = generate_password_hash(password)
        instance = cls(first_name=first_name, last_name=last_name,
                       email=email, username=username, password=password_hash, role=role)
        return instance

    @classmethod
    def get_by_username(cls, username):
        user = cls.query.filter(cls.username == username)
        return user

    @classmethod
    def validate_user(cls, username, password):
        user = cls.get_by_username(username=username)

        if user and user.check_password(password):
            return user

        return False

    def check_password(self, password):
        return check_password_hash(self.passwrod, password)

    def __repr__(self) -> str:
        return self.username
