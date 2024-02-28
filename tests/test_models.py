import os
import unittest
from unittest.mock import MagicMock

from RentikuSearch.models.base_model import Base
from RentikuSearch.models.database import Database
from RentikuSearch.models.models import Property, User


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_url = os.getenv("DATABASE_URL")
        self.db = Database(self.db_url)

    def test_init(self):
        self.assertEqual(self.db.db_url, self.db_url)

    def test_disconnect(self):
        self.db.session = MagicMock()
        self.db.disconnect()
        self.db.session.remove.assert_called_once()


class TestModels(unittest.TestCase):

    def setUp(self):
        self.db = Database(os.getenv("DATABASE_URL"))
        Base.metadata.drop_all(self.db.engine)
        self.db.reload()

    def tearDown(self):
        self.db.session.close()

    def test_user_model(self):
        user = User(
            username="test_user",
            email="test@example.com",
            password_hash="password123",
        )
        self.db.new(user)
        self.db.save()

        result = (
            self.db.session.query(User)
            .filter_by(username="test_user")
            .first()
        )
        self.assertEqual(result.email, "test@example.com")

    def test_property_model(self):
        user = User(
            username="test_user",
            email="test@example.com",
            password_hash="password123",
        )
        self.db.new(user)
        self.db.save()

        property = Property(
            title="Test Property",
            type="House",
            description="Test description",
            location="Test location",
            price=100000.0,
            owner_id=user.id,
        )

        property2 = Property(
            title="Test Property 2",
            type="Rental",
            description="Test description",
            location="Test location",
            price=150000.0,
            owner_id=user.id,
        )
        self.db.new(property)
        self.db.new(property2)

        self.db.save()

        result = (
            self.db.session.query(Property)
            .filter_by(title="Test Property")
            .first()
        )
        self.assertEqual(result.type, "House")
        self.assertEqual(result.price, 100000.0)
        self.assertEqual(result.owner_id, user.id)

        result = (
            self.db.session.query(Property).filter_by(type="Rental").first()
        )
        self.assertEqual(result.title, "Test Property 2")
        self.assertEqual(result.price, 150000.0)
        self.assertEqual(result.owner_id, user.id)


if __name__ == "__main__":
    unittest.main()
