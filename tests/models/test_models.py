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
        self.assertIsNone(self.db.session())
        self.db.reload()
        self.assertIsNotNone(self.db.session())
