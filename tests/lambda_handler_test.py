"""Unit tests for handling function."""
from copy import deepcopy
from mock import patch
import os
import unittest
from base64 import b64encode
from src.handler import lambda_handler


def create_event(authorization=None):
    """Create a sample lambda event from proxy integration."""
    event = {'resource': "/{proxy+}",
             'path': "test/hello",
             'httpMethod': "GET",
             'headers': {},
             'queryStringParameters': {},
             'pathParameters': {
                'proxy': "hello"
                },
             'stageVariables': {
                'stageVarName': "stageVarValue"
                },
             'requestContext': {},
             'body': "Some JSON string",
             'isBase64Encoded': False
             }

    headers = {}
    if authorization:
        headers.setdefault('Authorization', authorization)

    event['headers'] = headers

    return event


class MockContext(object):
    """Mock for an AWS lambda function context."""

    def __init__(self):
        """Initialize the mock object."""
        self.function_name = 'mock_lfs'
        self.function_version = '0.1'
        self.invoked_function_arn = 'arn:aws:lambda:us-east-1:3412431541'
        self.memory_limit_in_mb = 128
        self.aws_request_id = 31213131231312
        self.log_group_name = 'some group'
        self.log_stream_name = 'some stream'
        self.identity = None
        self.clientContext = None

    def get_remaining_time_millis():
        """Return remaining execution time."""
        return 10000


class HandlerFunctionTest(unittest.TestCase):
    """Unit tests for handling."""

    def test_invocation(self):
        """Test base invocation."""
        response = lambda_handler.lfs_handler(create_event(), MockContext())
        self.assertTrue(isinstance(response, dict))
        self.assertTrue('isBase64Encoded' in response)
        self.assertTrue('statusCode' in response)
        self.assertTrue('headers' in response)
        self.assertTrue('body' in response)

    @patch.dict(os.environ, {'USERNAME': 'PASSWORD'})
    def test_authorization(self):
        """Test the basic authorization flow."""
        # Testing a proper authentication
        auth = b64encode('USERNAME:PASWORD'.encode()).decode()
        event = deepcopy(create_event(authorization="Basic "+auth))
        print(event)
        response = lambda_handler.lfs_handler(event, MockContext())
        self.assertEqual(response['statusCode'], 200)
        # Testing a worng authentication
        event = create_event(authorization='ajdsadsasakjdsakjh')
        response = lambda_handler.lfs_handler(event, MockContext())
        self.assertEqual(response['statusCode'], 401)
        # Testing that no authentication fails
        response = lambda_handler.lfs_handler(create_event(), MockContext())
        self.assertEqual(response['statusCode'], 401)
