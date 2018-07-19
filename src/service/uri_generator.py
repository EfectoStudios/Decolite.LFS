"""Generates pre-signed uri's for blob handling."""
from boto3 import client
import os


s3_client = client('s3')


def create_uri(repo_name, resource_oid, upload=False, expires_in=300):
    """Create a download uri for the given oid and repo."""
    action = 'get_object'
    if upload:
        action = 'put_object'

    params = {'Bucket': os.environ['LFS_S3_BUCKET_NAME'],
              'Key': repo_name + '/' + resource_oid}
    return s3_client.generate_presigned_url(action, Params=params,
                                            ExpiresIn=expires_in)


def file_exists(repo_name, resource_oid):
    """Check if the file exists within the bucket."""
    key = repo_name + '/' + resource_oid
    response = s3_client.list_objects_v2(
                   Bucket=os.environ['LFS_S3_BUCKET_NAME'], Prefix=key)
    for obj in response.get('Contents', []):
        if obj['Key'] == key:
            return True
    return False
