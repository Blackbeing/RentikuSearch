from sqlalchemy.orm import declarative_base

import RentikuSearch.models as models

Base = declarative_base()


class BaseModel:

    def save(self):
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
