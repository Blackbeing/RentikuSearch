from sqlalchemy.ext.declarative import declarative_base

import RentikuSearch.models as models

Base = declarative_base()


class BaseModel:

    def __init__(self):
        pass

    def save(self):
        models.storage.new(self)
        models.storage.save()
