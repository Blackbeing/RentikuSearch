import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import sessionmaker

from RentikuSearch.models.database import Database
from RentikuSearch.models.models import Base, User, Property


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


class TestModels(unittest.TestCase):

    def setUp(self):
        self.db = Database(
            host="db",
            user="rsuser_test",
            password="password",
            dbname="rentikusearchdb_test",
        )
        self.db.connect()
        Base.metadata.drop_all(self.db.engine)
        Base.metadata.create_all(self.db.engine)
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_user_model(self):
        user = User(username='test_user',
                    email='test@example.com',
                    password_hash='password123')
        self.session.add(user)
        self.session.commit()

        result = self.session.query(User).filter_by(
            username='test_user').first()
        self.assertEqual(result.email, 'test@example.com')

    def test_property_model(self):
        user = User(username='test_user',
                    email='test@example.com',
                    password_hash='password123')
        self.session.add(user)
        self.session.commit()

        property = Property(title='Test Property',
                            type='House',
                            description='Test description',
                            location='Test location',
                            price=100000.0,
                            owner_id=user.id)

        property2 = Property(title='Test Property 2',
                             type='Rental',
                             description='Test description',
                             location='Test location',
                             price=150000.0,
                             owner_id=user.id)
        self.session.add(property)
        self.session.add(property2)

        self.session.commit()

        result = self.session.query(Property).filter_by(
            title='Test Property').first()
        self.assertEqual(result.type, 'House')
        self.assertEqual(result.price, 100000.0)
        self.assertEqual(result.owner_id, user.id)

        result = self.session.query(Property).filter_by(type="Rental").first()
        self.assertEqual(result.title, 'Test Property 2')
        self.assertEqual(result.price, 150000.0)
        self.assertEqual(result.owner_id, user.id)


if __name__ == "__main__":
    unittest.main()
