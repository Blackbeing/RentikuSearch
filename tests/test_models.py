import unittest

from RentikuSearch.models.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_init(self):
        self.assertIsNotNone(self.db.config)
        self.assertIsNotNone(self.db.db_url)
        self.assertIsNotNone(self.db._Database__engine)

    def test_reload(self):
        self.assertIsNone(self.db._Database__session)
        self.db.reload()
        self.assertIsNotNone(self.db._Database__session)

    def test_disconnect(self):
        self.assertIsNone(self.db._Database__session)
        self.db.reload()
        self.db.disconnect()
        self.db.db_url
        # self.db.reload()

    #     self.db.disconnect()
    #     self.assertIsNone(self.db._Database__session)
    #
    # def test_new(self):
    #     obj = MagicMock()
    #     self.db.new(obj)
    #     self.assertIn(obj, self.db._Database__session)
    #
    # def test_save(self):
    #     obj = MagicMock()
    #     self.db.reload()
    #     self.db.new(obj)
    #     self.db.save()
    #     self.assertIn(obj, self.db._Database__session)
    #
    # def test_delete(self):
    #     obj = MagicMock()
    #     self.db.reload()
    #     self.db.new(obj)
    #     self.db.delete(obj)
    #     self.assertNotIn(obj, self.db._Database__session)


if __name__ == "__main__":
    unittest.main()


# class TestModels(unittest.TestCase):
#
#     def setUp(self):
#         self.db = models.storage
#
#     def tearDown(self):
#         self.db.__session.close()
#
#     def test_storage(self):
#         print(self.db.db_url)
# def test_user_model(self):
#     user = User(
#         username="test_user",
#         email="test@example.com",
#         password_hash="password123",
#     )
#     self.db.new(user)
#     self.db.save()
#
#     result = (
#         self.db.__session.query(User)
#         .filter_by(username="test_user")
#         .first()
#     )
#     self.assertEqual(result.email, "test@example.com")
#
# def test_property_model(self):
#     user = User(
#         username="test_user",
#         email="test@example.com",
#         password_hash="password123",
#     )
#     self.db.new(user)
#     self.db.save()
#
#     property = Property(
#         title="Test Property",
#         type="House",
#         description="Test description",
#         location="Test location",
#         price=100000.0,
#         owner_id=user.id,
#     )
#
#     property2 = Property(
#         title="Test Property 2",
#         type="Rental",
#         description="Test description",
#         location="Test location",
#         price=150000.0,
#         owner_id=user.id,
#     )
#     self.db.new(property)
#     self.db.new(property2)
#
#     self.db.save()
#
#     result = (
#         self.db.__session.query(Property)
#         .filter_by(title="Test Property")
#         .first()
#     )
#     self.assertEqual(result.type, "House")
#     self.assertEqual(result.price, 100000.0)
#     self.assertEqual(result.owner_id, user.id)
#
#     result = (
#         self.db.__session.query(Property).filter_by(type="Rental").first()
#     )
#     self.assertEqual(result.title, "Test Property 2")
#     self.assertEqual(result.price, 150000.0)
#     self.assertEqual(result.owner_id, user.id)
#
#
# if __name__ == "__main__":
# unittest.main()
