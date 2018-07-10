"""Git authentication module."""
import os
from base64 import b64decode


def authorize(auth):
    """Decode the authorization header and authorize against the service."""
    auth_prefix = 'Basic '
    if auth_prefix not in auth:
        return False

    auth = auth.replace(auth_prefix, '')
    auth = b64decode(auth.encode()).decode()
    auth = auth.split(':')
    return authenticate(auth[0], auth[1])


def authenticate(username, password):
    """Authenticate the user against the service."""
    return os.environ['LFS_USERNAME'] == username and os.environ['LFS_PASSWORD'] == password  # noqa: E501
