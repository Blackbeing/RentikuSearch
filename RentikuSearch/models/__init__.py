import os

from config import get_config
from RentikuSearch.models import database

config = get_config()
database_url = config.DATABASE_URL

os.environ["DATABASE_URL"] = database_url
storage = database.Database(database_url)
storage.reload()
