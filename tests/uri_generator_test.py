"""Unit tests for uri generation."""
import unittest
from boto3 import resource, client
from moto import mock_s3
from src.service.uri_generator import create_uri


class URIGeneratorTest(unittest.TestCase):
    """Test case for uri generation from s3 buckets."""

    def setUp(self):
        """Set mock stub services for uri testing."""
        self.bucket_name = 'some-lfs'
        self.owner_name = 'SomeRandomGuy'
        self.repo_name = 'SomeRandomRepo'
        self.oid = 'SomeRandomOID'
        with mock_s3():
            # Create bucket.
            self.s3 = resource('s3')
            self.s3.create_bucket(Bucket=self.bucket_name)
            # Adding a file
            self.s3_client = client('s3', region_name='us-east-2')
            self.s3_client.put_object(Bucket='some-lfs',
                                      Key=self.owner_name + '/' + self.repo_name + '/' + self.oid,  # noqa: E501
                                      Body="Totally a binary file")

    def test_download_uri(self):
        """Verify that the uri is generated according to the file and repo."""
        url_regex = 'https://' + self.bucket_name + '.s3.amazonaws.com/'
        url_regex += self.owner_name + '/' + self.repo_name + '/' + self.oid

        self.assertTrue(url_regex in create_uri(self.bucket_name,
                                                self.owner_name,
                                                self.repo_name,
                                                self.oid))

    def test_upload_uri(self):
        """Verify that the uri is generated according to the file and repo."""
        url_regex = 'https://' + self.bucket_name + '.s3.amazonaws.com/'
        url_regex += self.owner_name + '/' + self.repo_name + '/' + self.oid

        self.assertTrue(url_regex in create_uri(self.bucket_name,
                                                self.owner_name,
                                                self.repo_name,
                                                self.oid,
                                                upload=True))
