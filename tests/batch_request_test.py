"""Unit tests for Batch API."""
import unittest
from src.service.batch_request import BatchConstants, BatchRequest, \
                                      BatchResponse


class BatchConstantsTest(unittest.TestCase):
    """Verifies that constant types are well defined."""

    def test_operations(self):
        """Verifies operations are well defined."""
        self.assertTrue(hasattr(BatchConstants, 'OPERATION_TYPES'))
        self.assertEqual(BatchConstants.OPERATION_TYPES['upload'],
                         'upload')
        self.assertEqual(BatchConstants.OPERATION_TYPES['download'],
                         'download')
        self.assertEqual(len(BatchConstants.OPERATION_TYPES), 2)

    def test_transfers(self):
        """Verifies tranfer types are well defined."""
        self.assertTrue(hasattr(BatchConstants, 'TRANSFER_TYPES'))
        self.assertEqual(BatchConstants.TRANSFER_TYPES['basic'], 'basic')
        self.assertGreaterEqual(len(BatchConstants.TRANSFER_TYPES), 1)


class BatchRequestTest(unittest.TestCase):
    """Test case for batch requests."""

    def test_attributes(self):
        """Verifies the request has the appropiate attributes."""
        req = BatchRequest(None, None, None)
        self.assertTrue(hasattr(req, 'operation'))
        self.assertTrue(hasattr(req, 'transfers'))
        self.assertTrue(hasattr(req, 'objects'))


class BatchResponseTest(unittest.TestCase):
    """Test case for batch responses."""

    def test_attributes(self):
        """Verifies the response has the appropiate attributes."""
        res = BatchResponse(None, None)
        self.assertTrue(hasattr(res, 'transfer'))
        self.assertTrue(hasattr(res, 'objects'))
