import unittest

from fastapi.testclient import TestClient

from RentikuSearch.api.v1.app import app


class TestUserEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = TestClient(app)

    def _create_user(self, username, email, password):
        data = {
            "username": username,
            "email": email,
            "password": password,
        }
        response = self.app.post("/api/v1/user", json=data)
        return response

    def test_create_user(self):
        response = self._create_user("John", "John@email", "password")
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["email"], "John@email")

    def test_get_all_users(self):
        response = self.app.get("/api/v1/user")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())
        self.assertNotEqual(len(response.json()), 0)
        self.assertIsInstance(response.json(), list)

    def test_get_user_by_id(self):
        response = self._create_user("Arnold", "arnold@email", "password")
        self.assertEqual(response.status_code, 201)
        user_id = response.json().get("id")
        response = self.app.get("/api/v1/user/{}".format(user_id))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())
        self.assertEqual(response.json().get("id"), user_id)
        self.assertEqual(response.json().get("email"), "arnold@email")


if __name__ == "__main__":
    unittest.main()
