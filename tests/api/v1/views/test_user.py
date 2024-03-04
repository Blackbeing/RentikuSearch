import unittest

from config import get_config
from RentikuSearch.api.v1.app import create_app


class TestUserEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ap = create_app(get_config())
        cls.app = cls.ap.test_client()

    def test_create_user(self):
        data = {
            "username": "John",
            "email": "John@email",
            "password_hash": "password",
        }
        response = self.app.post("/api/v1/user", json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_all_users(self):
        response = self.app.get("/api/v1/user")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)

    def test_get_user_by_id(self):
        response = self.app.get("/api/v1/user/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)


if __name__ == "__main__":
    unittest.main()
