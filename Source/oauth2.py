"""
This module groups classes related to Oauth 2.
"""

from abc import ABC, abstractmethod

from google.oauth2 import id_token
from google.auth.transport import requests


class BaseOAuth(ABC):  # pylint: disable=too-few-public-methods

    """
    Provides abstract methods that will be implemented by different
    Oauth providers class.
    """

    # (Receive token by HTTPS POST)
    # ...
    @abstractmethod
    def is_valid_token(self, token):
        """Performs token validation"""

    def __init__(self):
        pass


ANDROID_CLIENT_ID = "1044824317091-qqu2vn31igit3qvqkh363ctceo7ot75v.apps.googleusercontent.com"


class GoogleOAuth(BaseOAuth):  # pylint: disable=too-few-public-methods

    """Google OAuth 2.0"""

    def is_valid_token(self, token):
        """
        Performs token validation by calling google API. Google
        provided example code for token validation
        (https://developers.google.com/identity/sign-in/android/backend-auth)

        Args:
            token (string): token provided by client

        Returns:
            True when token is valid, False otherwise
        """

        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), ANDROID_CLIENT_ID)

            # Or, if multiple clients access the backend server:
            # idinfo = id_token.verify_oauth2_token(token, requests.Request())
            # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
            #     raise ValueError('Could not verify audience.')

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            # ID token is valid. Get the user's Google Account ID from the decoded token.
            userid = idinfo['sub']
            print(userid)
            return True
        except ValueError:
            # Invalid token
            print("ValueError")
            return False


def main():
    """Main program"""

    gaouth_object = GoogleOAuth()
    gaouth_object.is_valid_token("token")


if __name__ == "__main__":
    main()
