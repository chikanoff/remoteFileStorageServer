import os
import datetime as dt


dp = os.path.abspath(os.getcwd())


class DevelopmentConfig:
    # Basic configuration
    DEBUG = True
    SECRET_KEY = "secret"

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{dp}/dev_db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # flask_jwt_extended
    JWT_ACCESS_TOKEN_EXPIRES = dt.timedelta(minutes=1)

    # loguru configuration
    LOG_BACKTRACE = True
    LOG_LEVEL = "DEBUG"
    LOG_FILE = f"{dp}/logs/dev.log"

    # Files
    FILES_FOLDER = f"{dp}/static/files"


class ProductionConfig:
    # Basic configuration
    DEBUG = False
    SECRET_KEY = "secret"

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{dp}/prod_db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # loguru configuration
    LOG_BACKTRACE = True
    LOG_LEVEL = "INFO"
    LOG_FILE = f"{dp}/logs/prod.log"

    # Files
    FILES_FOLDER = f"{dp}/static/files"
