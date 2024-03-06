import json
from pathlib import Path

from RentikuSearch.models.database import Database
from RentikuSearch.models.models import Property, User

db = Database()
db.reload()
db.init_db()


def load_data(file_path, model_class):
    with file_path.open() as fd:
        data = json.load(fd)
        class_name = model_class.__name__.lower()
        class_plural = (
            class_name[:-1] + "ies"
            if class_name.endswith("y")
            else class_name + "s"
        )

        items = data.get(class_plural, {})
        for item_dict in items:
            item_dict.pop("id")
            item = model_class(**item_dict)
            db.new(item)
            db.save()


user_json_file = Path("users.json")
property_json_file = Path("property.json")

load_data(user_json_file, User)
load_data(property_json_file, Property)
