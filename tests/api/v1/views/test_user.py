import unittest

from fastapi.testclient import TestClient

from RentikuSearch.api.v1.app import app


class TestUserEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = TestClient(app)

    def test_create_user(self):
        data = {
            "username": "John",
            "email": "John@email",
            "password": "password",
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
