"""Git authentication module."""
import os
from base64 import b64decode


def authenticate(auth):
    """Decode the authorization header and authorize against the service."""
    auth_prefix = 'Basic '
    if auth_prefix not in auth:
        return False

    auth = auth.replace(auth_prefix, '')
    auth = b64decode(auth.encode()).decode()
    auth = auth.split(':')
    return os.environ['LFS_USERNAME'] == auth[0] and os.environ['LFS_PASSWORD'] == auth[1]  # noqa: E501
