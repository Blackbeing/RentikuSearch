import unittest

from fastapi.testclient import TestClient

from RentikuSearch.api.v1.app import app


class TestPropertyEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = TestClient(app)

    def test_create_property(self):
        user_data = {
            "username": "Anderson",
            "email": "anderson@email",
            "password": "password",
        }
        response = self.app.post("/api/v1/user", json=user_data)
        property_data = {
            "title": "Title",
            "description": "Description",
            "action": "rent",
            "price": "2222",
            "rent": "0",
            "num_rooms": "4",
            "address": "Address",
            "latitude": "23.23232",
            "longitude": "34.2342",
            "region": "Region",
            "image_url": "Img url",
            "owner_id": response.json()["id"],
        }
        # print(property_data)
        response = self.app.post("/api/v1/property", json=property_data)
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json())
        self.assertEqual(response.json()["title"], "Title")

    #

    def test_get_all_propertys(self):
        response = self.app.get("/api/v1/property")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())
        self.assertIsInstance(response.json(), list)
        self.assertEqual(response.json()[0]["region"], "Region")

    #

    def test_get_property_by_id(self):
        response = self.app.get("/api/v1/property/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()["region"], "Region")
        self.assertEqual(response.json()["longitude"], "34.2342")


#
#
if __name__ == "__main__":
    unittest.main()
