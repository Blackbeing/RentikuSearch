import RentikuSearch.models as models


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

    def __repr__(self):
        return "[{}:{}] {}".format(
            self.__class__.__name__, self.id, self.to_dict()
        )
