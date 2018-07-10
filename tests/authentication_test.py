"""Unit tests for authentication."""
from base64 import b64encode
from mock import patch
import os
import unittest
from src.service.authentication import authenticate, authorize


class AuthenticationTest(unittest.TestCase):
    """Test case for git authentication via https."""

    @patch.dict(os.environ, {'LFS_USERNAME': 'user', 'LFS_PASSWORD': 'pass'})
    def test_credentials(self):
        """Test the service authenticates against environment variables."""
        self.assertTrue(authenticate(os.environ['LFS_USERNAME'],
                                     os.environ['LFS_PASSWORD']))
        self.assertFalse(authenticate('sutano', 'unaClaveMuySegura'))

    @patch.dict(os.environ, {'LFS_USERNAME': 'user', 'LFS_PASSWORD': 'pass'})
    def test_authorization(self):
        """Test authorization of the service."""
        self.assertFalse(authorize(''))

        auth = os.environ['LFS_USERNAME'] + ':' + os.environ['LFS_PASSWORD']
        auth = b64encode(auth.encode()).decode()
        auth = 'Basic ' + auth
        self.assertTrue(authorize(auth))

        auth = b64encode('sutano:unaClaveMuySegura'.encode()).decode()
        self.assertFalse(authorize('Basic '+auth))
