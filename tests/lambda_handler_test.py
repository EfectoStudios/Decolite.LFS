"""Unit tests for handling function."""
import unittest
from src.handler import lambda_handler


class HandlerFunctionTest(unittest.TestCase):
    """Unit tests for handling."""

    def test_invocation(self):
        """Test base invocation."""
        self.assertIsNone(lambda_handler.lfs_handler(None, None))
        pass
