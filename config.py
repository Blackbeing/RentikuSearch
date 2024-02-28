import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
basedir = Path(__file__).parent


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("RENTIKUSEARCH_SK")
    DATABASE_URL = os.getenv("RENTIKUSEARCH_DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    TESTING = True
    DATABASE_URL = os.getenv("RENTIKUSEARCH_DB_URL_TEST")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE_URL = os.getenv("RENTIKUSEARCH_DB_URL_DEV")


def get_config(env_str="development"):
    config_dict = {
        "production": BaseConfig,
        "development": DevelopmentConfig,
        "testing": TestingConfig,
    }
    return config_dict.get(env_str)
