import os
from dotenv import load_dotenv


def read_credentails():
    """
    Return users credentials from the environnement variable
    raise a an exception if the credentials are empty

    Raises:
        NotImplementedError: [description]
    """
    load_dotenv()

    USER_EMAIL = os.getenv("USER_EMAIL")
    USER_PASSWORD = os.getenv("USER_PASSWORD")
    if USER_EMAIL and USER_PASSWORD:
        return USER_EMAIL, USER_PASSWORD
    else:
        raise ValueError(
            'Please add a .env file and put the credentials on it,\
                         refer to the sample')
