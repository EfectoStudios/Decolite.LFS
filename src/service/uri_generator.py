"""Generates pre-signed uri's for blob handling."""
from boto3 import client


def create_download_uri(bucket_name, repo_name, resource_oid, expires_in=300):
    """Create a download uri for the given oid and repo."""
    s3_client = client('s3')
    params = {'Bucket': bucket_name,
              'Key': repo_name + '/' + resource_oid}
    return s3_client.generate_presigned_url('get_object', Params=params,
                                            ExpiresIn=expires_in)


def create_upload_uri(bucket_name, repo_name, resource_oid, expires_in=300):
    """Create an upload uri for a new oid."""
    s3_client = client('s3')
    params = {'Bucket': bucket_name,
              'Key': repo_name + '/' + resource_oid}
    return s3_client.generate_presigned_url('put_object', Params=params,
                                            ExpiresIn=expires_in)
