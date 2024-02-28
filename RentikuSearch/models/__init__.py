import os

from config import get_config
from RentikuSearch.models import database

config = get_config()
os.environ["SQLALCHEMY_DATABASE_URL"] = config.__dict__[
    "SQLALCHEMY_DATABASE_URL"
]

storage = database.Database(os.environ["SQLALCHEMY_DATABASE_URL"])
storage.reload()
