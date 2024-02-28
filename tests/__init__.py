import os

from config import get_config

config = get_config("testing")
os.environ["DATABASE_URL"] = config.DATABASE_URL
