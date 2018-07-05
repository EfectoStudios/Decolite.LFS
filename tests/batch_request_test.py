"""Unit tests for Batch API."""
import json
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
        self.assertEqual(BatchConstants.OPERATION_TYPES['verify'],
                         'verify')
        self.assertEqual(len(BatchConstants.OPERATION_TYPES), 3)

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

    def test_str(self):
        """Test str() function equal JSON dump."""
        test_data = {'foo': 'bar', 'foo2': ['hello', 'world']}
        wrapper = JSONWrapper()
        wrapper._data = test_data
        self.assertEqual(str(wrapper), json.dumps(test_data))


class BatchActionTest(unittest.TestCase):
    """Test case for batch actions."""

    def test_attributes(self):
        """Verify the action has the corresponding attributes."""
        action = BatchAction()
        data = action.get_data()

        self.assertTrue('download' in data or 'upload' in data)
        self.assertEqual(len(data), 1)

        self.assertTrue('href' in list(data.values())[0])
        self.assertTrue('expires_in' in list(data.values())[0])


class BatchObjectTest(unittest.TestCase):
    """Test case for a batch object."""

    def test_attributes(self):
        """Verify the object has the corresponding attributes."""
        obj = BatchObject()
        self.assertTrue('oid' in obj.get_data())
        self.assertTrue('size' in obj.get_data())
        self.assertFalse('actions' in obj.get_data())

        acts = [BatchAction()]
        obj = BatchObject(actions=acts)
        self.assertTrue('oid' in obj.get_data())
        self.assertTrue('size' in obj.get_data())
        self.assertTrue('actions' in obj.get_data())


class BatchRequestTest(unittest.TestCase):
    """Test case for batch requests."""

    def test_attributes(self):
        """Verifies the request has the appropiate attributes."""
        req = BatchRequest()
        self.assertTrue('transfers' in req.get_data())
        self.assertTrue('operation' in req.get_data())
        self.assertTrue('objects' in req.get_data())


class BatchResponseTest(unittest.TestCase):
    """Test case for batch responses."""

    def test_attributes(self):
        """Verifies the response has the appropiate attributes."""
        res = BatchResponse()
        self.assertTrue('transfer' in res.get_data())
        self.assertTrue('objects' in res.get_data())

    def test_default_values(self):
        """Test that the default values are correct and well typed."""
        res = BatchResponse()
        self.assertTrue(res.get_data()['transfer'],
                        BatchConstants.TRANSFER_TYPES['basic'])
        self.assertEqual(res.get_data()['objects'], [])
