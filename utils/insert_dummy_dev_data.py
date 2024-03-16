#!/usr/bin/python

import random
from pathlib import Path

from faker import Faker

from RentikuSearch import dependancies as dp
from RentikuSearch.models.database import Database
from RentikuSearch.models.models import Property, User

fake = Faker()

db_c = Database()
db_c.drop_tables()
db_c.init_db()
db = db_c.session


def get_img_url():
    property_images = list(
        (
            Path(__file__).parent.parent
            / "RentikuSearch"
            / "web_fastapi"
            / "static"
            / "images"
            / "properties"
        ).iterdir()
    )
    image_url = random.choice(property_images)
    p = "/".join(image_url.parts[-3:])
    image_url = "/{}".format(p)
    return image_url


def create_user_and_property():
    fn = fake.first_name()
    ln = fake.last_name()
    username = "{}_{}".format(fn, ln)
    email = "{}@{}".format(username, fake.domain_name())
    password = dp.hash_password(fake.password())
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)

    property = Property(
        title=fake.company(),
        description=fake.catch_phrase(),
        action=["sell", "rent", "lease"][
            random.randint(0, 2)
        ],  # Pick random action
        price=fake.pyint(min_value=10000, max_value=1000000),
        rent=fake.pyint(min_value=1000, max_value=5000),
        num_rooms=fake.pyint(min_value=1, max_value=5),
        address=fake.address(),
        latitude=str(fake.latitude()),
        longitude=str(fake.longitude()),
        region=fake.country(),
        image_url=get_img_url(),
        owner_id=user.id,  # Link property to user
    )
    db.add(property)
    db.commit()
    db.refresh(property)

    return user, property


if __name__ == "__main__":
    for _ in range(10):
        create_user_and_property()
