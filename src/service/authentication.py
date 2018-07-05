"""Git authentication module."""
import os


def authenticate(username, password):
    """Authenticate the user against the service."""
    if username not in os.environ:
        return False
    return os.environ[username] == password
