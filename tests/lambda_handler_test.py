"""Unit tests for handling function."""
import unittest
from src.handler import lambda_handler


def create_event():
    """Create a sample lambda event from proxy integration."""
    return {'path': "test/hello",
            'headers': {},
            'pathParameters': {
                    'proxy': "hello"
                },
            'requestContext': {},
            'resource': "/{proxy+}",
            'httpMethod': "GET",
            'queryStringParameters': {},
            'stageVariables': {
                    'stageVarName': "stageVarValue"
                }
            }


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
        self.assertTrue('statusCode' in response)
        self.assertTrue('headers' in response)
        self.assertTrue('body' in response)
