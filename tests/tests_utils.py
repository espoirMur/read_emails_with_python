from unittest import TestCase
from unittest.mock import patch, call
from utils import read_credentails


class TestUtilsReadCredentials(TestCase):
    @patch('utils.getenv', return_value='Somecredentials')
    @patch('utils.load_dotenv', return_value=None)
    def test_can_read_an_return_credentials(self, load_env_mock, get_env_mock):
        """
        test if we can read and return credentials
        Args:
            TestCase ([type]): [description]
        """
        read_credentails()
        env_variables = [call("USER_EMAIL"), call("USER_PASSWORD")]
        load_env_mock.assert_called_once()
        get_env_mock.assert_has_calls(env_variables, any_order=True)

    @patch('utils.getenv', return_value=None)
    @patch('utils.load_dotenv', return_value=None)
    def test_raise_value_error_when_env_is_null(
            self, load_env_mock, get_env_mock):
        self.assertRaises(ValueError, read_credentails)
        load_env_mock.assert_called_once()
