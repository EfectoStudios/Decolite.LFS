"""Unit tests for Batch API."""
import unittest
from src.service.batch_request import BatchConstants


class BatchConstantsTest(unittest.TestCase):
    """Verifies that constant types are well defined."""

    def test_operations(self):
        """Verifies operations are well defined."""
        self.assertTrue(hasattr(BatchConstants, 'OPERATION_TYPES'))
        self.assertEqual(BatchConstants.OPERATION_TYPES['upload'],
                         'upload')
        self.assertEqual(BatchConstants.OPERATION_TYPES['download'],
                         'download')
        self.assertEqual(BatchConstants.OPERATION_TYPES['verify'],
                         'verify')
        self.assertEqual(len(BatchConstants.OPERATION_TYPES), 3)

    def test_transfers(self):
        """Verifies tranfer types are well defined."""
        self.assertTrue(hasattr(BatchConstants, 'TRANSFER_TYPES'))
        self.assertEqual(BatchConstants.TRANSFER_TYPES['basic'], 'basic')
        self.assertGreaterEqual(len(BatchConstants.TRANSFER_TYPES), 1)
