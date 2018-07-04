"""Unit tests for uri generation."""
import json
import unittest
from botocore.exceptions import ClientError
from moto import mock_s3
import src.service.uri_generator


class URIGeneratorTest(unittest.TestCase):
    """Test case for uri generation from s3 buckets."""

    def test_download_uri(self):
        """Verify that the uri is generated according to the file and repo."""
        self.fail('test not implemented')

    def test_upload_uri(self):
        """Verify that the uri is generated according to the file and repo."""
        self.fail('test not implemented')

    def test_folder_creation(self):
        """
        Test the lambda is able to create a new folder corresponding
        to a new repo.
        """
        self.fail('test not implemented')
