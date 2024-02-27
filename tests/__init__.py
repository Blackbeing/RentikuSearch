import os

from config import get_config

config = get_config("testing")
os.environ["SQLALCHEMY_DATABASE_URL"] = config.__dict__[
    "SQLALCHEMY_DATABASE_URL"
]
