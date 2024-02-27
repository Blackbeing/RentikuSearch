import unittest
from unittest.mock import MagicMock

from RentikuSearch.models.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database(
            host="db",
            user="rsuser_test",
            password="password",
            dbname="rentikusearchdb_test",
        )
        self.db.conn = MagicMock()
        self.db.cursor = MagicMock()

    def test_connect(self):
        self.db.connect()
        self.assertIsNotNone(self.db.conn)
        self.assertIsNotNone(self.db.cursor)
        self.assertIsNotNone(self.db.engine)

    def test_disconnect(self):
        self.db.disconnect()
        self.db.conn.close.assert_called_once()

    def test_execute(self):
        query = "SELECT * FROM table"
        self.db.execute(query)
        self.db.cursor.execute.assert_called_once_with(query)
        self.db.conn.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
