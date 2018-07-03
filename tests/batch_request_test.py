"""Unit tests for Batch API."""
import unittest
from src.service.batch_request import BatchConstants, JSONWrapper, \
                                      BatchAction, BatchObject, \
                                      BatchRequest, BatchResponse


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


class JSONWrapperTest(unittest.TestCase):
    """Test case for the JSON wrapper."""

    def test_attributes(self):
        """Verify the initialized object possesses a dictionary."""
        wrapper = JSONWrapper()
        self.assertIsNotNone(wrapper._data)

    def test_getter(self):
        """Test the getter function."""
        wrapper = JSONWrapper()
        self.assertDictEqual(wrapper.get_data(), {})


class BatchActionTest(unittest.TestCase):
    """Test case for batch actions."""

    def test_attributes(self):
        """Verify the action has the corresponding attributes."""
        action = BatchAction()
        self.assertTrue('download' in action.get_data() or
                        'upload' in action.get_data())
        self.assertEqual(len(action.get_data()), 1)


class BatchObjectTest(unittest.TestCase):
    """Test case for a batch object."""

    def test_attributes(self):
        """Verify the object has the corresponding attributes."""
        obj = BatchObject(isResponse=False)
        self.assertTrue('oid' in obj.get_data())
        self.assertTrue('size' in obj.get_data())
        self.assertFalse('actions' in obj.get_data())

        obj = BatchObject(isResponse=True)
        self.assertTrue('oid' in obj.get_data())
        self.assertTrue('size' in obj.get_data())
        self.assertTrue('actions' in obj.get_data())


class BatchRequestTest(unittest.TestCase):
    """Test case for batch requests."""

    def test_attributes(self):
        """Verifies the request has the appropiate attributes."""
        req = BatchRequest(None, None, None)
        self.assertTrue('transfers' in req.get_data())
        self.assertTrue('operation' in req.get_data())
        self.assertTrue('objects' in req.get_data())


class BatchResponseTest(unittest.TestCase):
    """Test case for batch responses."""

    def test_attributes(self):
        """Verifies the response has the appropiate attributes."""
        res = BatchResponse(None, None)
        self.assertTrue('transfer' in res.get_data())
        self.assertTrue('objects' in res.get_data())
