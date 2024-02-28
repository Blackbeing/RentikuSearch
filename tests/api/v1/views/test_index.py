import unittest

from config import get_config
from RentikuSearch.api.v1.app import create_app


class TestStatusEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(get_config("testing")).test_client()

    def test_status_endpoint(self):
        response = self.app.get("/api/v1/status")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Alive")


if __name__ == "__main__":
    unittest.main()
