from unittest.mock import Mock, MagicMock


class MockIMAP4SSL:

    def __init__(self, host):
        self.host = host

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    login = Mock(return_value=None)
    list = Mock(return_value=None)
    select = Mock(return_value=None)
    search = Mock(
        return_value=(
            'OK', [
                bytes(
                    'this is a mail test', encoding='UTF-8')]))
    fetch = Mock(return_value=(
        'OK', [['', bytes('this is a mail test', encoding='UTF-8')]]))
    store = Mock(return_value=(
        'OK', [['', bytes('this is a mail test', encoding='UTF-8')]]))
