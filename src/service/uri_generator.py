"""Generates pre-signed uri's for blob handling."""
from boto3 import client
import os


def create_uri(owner_name, repo_name, resource_oid,
               upload=False, expires_in=300):
    """Create a download uri for the given oid and repo."""
    action = 'get_object'
    if upload:
        action = 'put_object'

    s3_client = client('s3')
    params = {'Bucket': os.environ['LFS_S3_BUCKET_NAME'],
              'Key': owner_name + '/' + repo_name + '/' + resource_oid}
    return s3_client.generate_presigned_url(action, Params=params,
                                            ExpiresIn=expires_in)
