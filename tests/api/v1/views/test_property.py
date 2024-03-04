import unittest

from config import get_config
from RentikuSearch.api.v1.app import create_app


class TestPropertyEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ap = create_app(get_config())
        cls.app = cls.ap.test_client()

    def test_create_property(self):
        data = {
            "username": "Anderson",
            "email": "anderson@email",
            "password_hash": "password",
        }
        response = self.app.post("/api/v1/user", json=data)
        data = {
            "title": "TestProperty",
            "type": "Rental",
            "description": "A well spaced rental home",
            "location": "2929293232",
            "price": 23323,
            "owner_id": response.json.get("id"),
        }
        response = self.app.post("/api/v1/property", json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_all_propertys(self):
        response = self.app.get("/api/v1/property")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)

    def test_get_property_by_id(self):
        response = self.app.get("/api/v1/property/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json())


if __name__ == "__main__":
    unittest.main()
