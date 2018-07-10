"""Function invocation module."""


def lfs_handler(event, context):
    """Handle git lfs requests sent through API Gateway."""
    if 'Authorization' not in event['headers']:
        status_code = 401
    return None


def create_response(status_code=200, bacth_request=None):
    """Create the response according to the given parameters."""
    default_headers = {'Accept': "application/vnd.git-lfs+json",
                       'Content-Type': "application/vnd.git-lfs+json"}
    response = {'isBase64Encoded': False,
                'statusCode': status_code,
                'headers': default_headers}
    return response


def base_handler():
    """Return the root of lfs repo."""


def batch_handler():
    """Handle batch requests."""


def lock_handler():
    """Handle lock requests. Currently not supported."""
