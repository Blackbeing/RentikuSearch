import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
basedir = Path(__file__).parent


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("RENTIKUSEARCH_SK")
    SQLALCHEMY_DATABASE_URI = os.environ.get("RENTIKUSEARCH_DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://rsuser_test:password@db:5432/rentikusearchdb_test"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://rsuser_dev:password@db:5432/rentikusearchdb_dev"


def get_config(env_str="development"):
    config_dict = {
        "production": BaseConfig,
        "development": DevelopmentConfig,
        "testing": TestingConfig,
    }
    return config_dict.get(env_str)
