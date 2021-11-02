from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

db = SQLAlchemy()
api = Api(doc="/swagger")
jwt = JWTManager()
bcrypt = Bcrypt()
socketio = SocketIO()
