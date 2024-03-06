import unittest

from fastapi.testclient import TestClient

from RentikuSearch.api.v1.app import app


class TestStatusEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = TestClient(app)

    def test_status_endpoint(self):
        response = self.app.get("/api/v1/status")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Alive")


if __name__ == "__main__":
    unittest.main()
