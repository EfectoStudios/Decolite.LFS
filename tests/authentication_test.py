"""Unit tests for authentication."""
from mock import patch
import os
import unittest
from src.service.authentication import authenticate


class AuthenticationTest(unittest.TestCase):
    """Test case for git authentication via https."""

    @patch.dict(os.environ, {'USERNAME': 'PASSWORD'})
    def test_credentials(self):
        """Test the service authenticates against environment variables."""
        self.assertTrue(authenticate('USERNAME', os.environ['USERNAME']))
        self.assertFalse(authenticate('sutano', 'unaClaveMuySegura'))
