import unittest
from unittest.mock import Mock, patch

from RentikuSearch.models import models, schemas
from RentikuSearch.models.crud import (create_user, delete_user_by_id,
                                       get_user_by_email, get_user_by_id,
                                       get_user_by_username, get_users,
                                       update_user)


class TestCRUDFunctions(unittest.TestCase):

    @patch("RentikuSearch.models.crud.create_user")
    @patch("RentikuSearch.models.crud.dp.hash_password")
    def test_create_user(self, mock_hash_password, mock_create_user):
        mock_db = Mock()
        mock_user = Mock()

        result = create_user(mock_db, mock_user)
        mock_hash_password.assert_called_once_with(mock_user.password)
        self.assertEqual(mock_user.username, result.username)

    @patch("RentikuSearch.models.crud.Session")
    def test_get_user_by_id(self, mock_session):
        id = 1
        mock_query = Mock()
        mock_session.return_value.query.return_value = mock_query

        test_user = models.User(
            id=id, username="username", email="email@email"
        )
        mock_query.filter_by.return_value.first.return_value = test_user

        user = get_user_by_id(mock_session.return_value, id=id)
        self.assertEqual(user, test_user)
        mock_session.return_value.query.assert_called_once_with(models.User)
        mock_query.filter_by.assert_called_once_with(id=id)
        mock_query.filter_by.return_value.first.assert_called_once()

    @patch("RentikuSearch.models.crud.Session")
    def test_get_user_by_email(self, mock_session):
        email = "email@email"
        mock_query = Mock()
        mock_session.return_value.query.return_value = mock_query

        test_user = models.User(id=1, username="username", email=email)
        mock_query.filter_by.return_value.first.return_value = test_user

        user = get_user_by_email(
            mock_session.return_value, email="email@email"
        )
        self.assertEqual(user, test_user)
        mock_session.return_value.query.assert_called_once_with(models.User)
        mock_query.filter_by.assert_called_once_with(email=email)
        mock_query.filter_by.return_value.first.assert_called_once()

    @patch("RentikuSearch.models.crud.Session")
    def test_get_user_by_username(self, mock_session):
        username = "username"
        mock_query = Mock()
        mock_session.return_value.query.return_value = mock_query

        test_user = models.User(id=1, username=username, email="email@email")
        mock_query.filter_by.return_value.first.return_value = test_user

        user = get_user_by_username(
            mock_session.return_value, username=username
        )
        self.assertEqual(user, test_user)
        mock_session.return_value.query.assert_called_once_with(models.User)
        mock_query.filter_by.assert_called_once_with(username=username)
        mock_query.filter_by.return_value.first.assert_called_once()

    @patch("RentikuSearch.models.crud.Session")
    def test_get_users(self, mock_session):
        mock_query = Mock()
        mock_session.return_value.query.return_value = mock_query
        test_user = models.User(
            id=1, username="username", email="email@email"
        )
        mock_query.offset.return_value.limit.return_value.all.return_value = [
            test_user
        ]
        users = get_users(db=mock_session.return_value)
        self.assertIsInstance(users, list)
        mock_session.return_value.query.assert_called_once_with(models.User)
        mock_session.return_value.query.return_value.offset.assert_called_once_with(
            0
        )
        mock_session.return_value.query.return_value.offset.return_value.limit.assert_called_once_with(
            50
        )
        mock_session.return_value.query.return_value.offset.return_value.limit.return_value.all.assert_called_once()

    @patch("RentikuSearch.models.crud.dp.hash_password")
    @patch("RentikuSearch.models.crud.Session")
    def test_update_user(self, mock_session, mock_hash_password):
        mock_user = Mock()
        update_data = schemas.UserUpdate(password="new_password")

        mock_hash_password.return_value = "hashed_password"

        mock_session.return_value.commit.return_value = None
        mock_session.return_value.refresh.return_value = None

        updated_user = update_user(
            mock_session.return_value, mock_user, update_data
        )

        mock_hash_password.assert_called_once_with("new_password")
        mock_session.return_value.commit.assert_called_once()
        mock_session.return_value.refresh.assert_called_once_with(mock_user)
        self.assertEqual(updated_user.email, mock_user.email)

    @patch("RentikuSearch.models.crud.get_user_by_id")
    @patch("RentikuSearch.models.crud.Session")
    def test_delete_user(self, mock_session, mock_get_user_by_id):
        mock_user = Mock()
        mock_get_user_by_id.return_value = mock_user
        mock_session.return_value.delete.return_value = None
        mock_session.return_value.commit.return_value = None

        delete_user_by_id(db=mock_session.return_value, id=mock_user.id)
        mock_get_user_by_id.assert_called_once()
        mock_session.return_value.delete.assert_called_once_with(mock_user)
        mock_session.return_value.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
