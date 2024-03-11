# can be run from base dir using
# python -m utils.insert_dummy_dev_data
import json
from pathlib import Path

from RentikuSearch.models.database import Database
from RentikuSearch.models.models import Property, User

base_path = Path(__file__).parent

db_c = Database()
db_c.drop_tables()
db_c.init_db()
db = db_c.session()


def load_data(file_path):
    with file_path.open() as fd:
        data = json.load(fd)
        properties = data.get("properties", [])
        users = data.get("users", [])

        for user_dict in users:
            user_dict.pop("id")
            user = User(**user_dict)
            db.add(user)
        db.commit()

        for property_dict in properties:
            property_dict.pop("id")
            property = Property(**property_dict)
            db.add(property)
        db.commit()


db_json_file = base_path / "db.json"

load_data(db_json_file)
