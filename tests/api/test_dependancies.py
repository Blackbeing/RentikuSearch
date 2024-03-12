import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import Mock, patch

from RentikuSearch.dependancies import (authenticate_user,
                                        create_access_token, hash_password,
                                        verify_password)


class TestPasswordFunctions(unittest.TestCase):

    @patch("RentikuSearch.dependancies.pwd_context")
    def test_hash_password(self, mock_pwd_context):
        mock_hash_method = Mock(return_value="mocked_hash_password")
        mock_pwd_context.hash = mock_hash_method

        password = "test_password"
        hashed_password = hash_password(password)
        mock_hash_method.assert_called_once_with(password)
        self.assertEqual(hashed_password, "mocked_hash_password")

    @patch("RentikuSearch.dependancies.pwd_context")
    def test_verify_password(self, mock_pwd_context):
        mock_verify_method = Mock(return_value=True)
        mock_pwd_context.verify = mock_verify_method

        password = "test_password"
        hashed_password = "test_hashed_password"
        verify = verify_password(password, hashed_password)
        mock_verify_method.assert_called_once_with(password, hashed_password)
        self.assertEqual(verify, True)

    @patch("RentikuSearch.dependancies.pwd_context")
    def test_verify_wrong_password(self, mock_pwd_context):
        mock_verify_method = Mock(return_value=False)
        mock_pwd_context.verify = mock_verify_method

        password = "test_password"
        hashed_password = "wrong_hashed_password"
        verify = verify_password(password, hashed_password)
        mock_verify_method.assert_called_once_with(password, hashed_password)
        self.assertEqual(verify, False)

    @patch("RentikuSearch.dependancies.jwt.encode")
    def test_create_access_token_with_delta(self, mock_jwt_encode):

        mock_jwt_encode.return_value = "mocked_encoded_jwt"
        data = {"sub": "test_user"}
        to_encode = data.copy()
        expires_delta = timedelta(days=7)
        encoded_jwt = create_access_token(to_encode, expires_delta)
        self.assertEqual(encoded_jwt, "mocked_encoded_jwt")

        data.update({"exp": datetime.now(timezone.utc) + expires_delta})
        mock_jwt_encode.assert_called()
        # mock_jwt_encode.assert_called_once_with(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @patch("RentikuSearch.dependancies.jwt.encode")
    def test_create_access_token_without_delta(self, mock_jwt_encode):

        mock_jwt_encode.return_value = "mocked_encoded_jwt"
        data = {"sub": "test_user"}
        encoded_jwt = create_access_token(data.copy())
        self.assertEqual(encoded_jwt, "mocked_encoded_jwt")
        mock_jwt_encode.assert_called()
        # mock_jwt_encode.assert_called_once_with(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @patch("RentikuSearch.dependancies.verify_password")
    @patch("RentikuSearch.models.crud.get_user_by_username")
    def test_authenticate_user(
        self, mock_get_user_by_username, mock_verify_password
    ):
        mock_user = Mock()
        mock_get_user_by_username.return_value = mock_user

        mock_verify_password.return_value = True

        mock_db = Mock()
        result = authenticate_user(mock_db, "username", "password")
        mock_get_user_by_username.assert_called_once_with(mock_db, "username")

        mock_verify_password.assert_called_once_with(
            "password", mock_user.password
        )
        self.assertEqual(mock_user, result)

    @patch("RentikuSearch.dependancies.verify_password")
    @patch("RentikuSearch.models.crud.get_user_by_username")
    def test_authenticate_nonexistent_user(
        self, mock_get_user_by_username, mock_verify_password
    ):
        mock_db = Mock()
        mock_get_user_by_username.return_value = None

        result = authenticate_user(mock_db, "nonexistentuser", "nonpassword")
        mock_get_user_by_username.assert_called_once_with(
            mock_db, "nonexistentuser"
        )
        mock_verify_password.assert_not_called()
        self.assertFalse(result)

    @patch("RentikuSearch.dependancies.verify_password")
    @patch("RentikuSearch.models.crud.get_user_by_username")
    def test_authenticate_wrong_password(
        self, mock_get_user_by_username, mock_verify_password
    ):
        mock_user = Mock()
        mock_get_user_by_username.return_value = mock_user

        mock_verify_password.return_value = False

        mock_db = Mock()
        result = authenticate_user(mock_db, "username", "wrong_password")
        mock_get_user_by_username.assert_called_once_with(mock_db, "username")
        mock_verify_password.assert_called_once_with(
            "wrong_password", mock_user.password
        )

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
