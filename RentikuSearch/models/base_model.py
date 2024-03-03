from sqlalchemy.orm import declarative_base

import RentikuSearch.models as models

Base = declarative_base()


class BaseModel:

    def save(self):
        models.storage.new(self)
        models.storage.save()
