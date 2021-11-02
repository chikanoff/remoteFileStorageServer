import os
import logging

from loguru import logger
from flask import Flask
from dotenv import load_dotenv
from sqlalchemy_utils.functions import database_exists

from conduit.extensions import db, api, jwt, bcrypt, socketio
from conduit.config import DevelopmentConfig, ProductionConfig


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Retrieve context where the logging call occurred, this happens to be in the 6th frame upward
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


def create_app(config=None):
    load_dotenv()

    if config is None:
        if os.environ.get("FLASK_ENV") and os.environ.get("FLASK_ENV").upper() == "PRODUCTION":
            config = ProductionConfig
        else:
            config = DevelopmentConfig

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    logger.start(
        app.config["LOG_FILE"],
        level=app.config["LOG_LEVEL"],
        backtrace=app.config["LOG_BACKTRACE"],
        rotation="10 MB",
    )
    app.logger.addHandler(InterceptHandler())

    # register all extension
    register_extensions(app)

    return app


def register_extensions(app: Flask):
    jwt.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    socketio.init_app(app)

    # register models
    from conduit.models.user import User

    # register sockets
    from conduit.sockets.ping import connect

    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        with app.app_context():
            db.create_all()

    api.init_app(app)
    # register namespaces
    from conduit.api.users import ns as users_ns
    from conduit.api.auth import ns as auth_ns

    api.add_namespace(users_ns, "/api/users")
    api.add_namespace(auth_ns, "/api/auth")
