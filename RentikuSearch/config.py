import os

from pydantic_settings import BaseSettings


class Base(BaseSettings):
    DEBUG: bool
    TESTING: bool
    SECRET_KEY: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: str
    DB_DRIVERNAME: str = "postgresql+psycopg2"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = "RentikuSearch/.env"


class DevSettings(Base):

    class Config:
        env_file = "RentikuSearch/.env_dev"


class TestSettings(Base):

    class Config:
        env_file = "RentikuSearch/.env_test"


#
settings_dict = {
    "dev": DevSettings,
    "test": TestSettings,
}
#
settings = settings_dict.get(os.getenv("RS_ENV"), DevSettings)()
