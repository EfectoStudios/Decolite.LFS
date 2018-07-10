"""Function invocation module."""
from routes import get_path_request


def lfs_handler(event, context):
    """Handle git lfs requests sent through API Gateway."""
    if 'Authorization' not in event['headers']:
        return create_response(status_code=401)

    path = event['path']
    owner, repo, type = get_path_request(path)

    if type == 'BASE':
        res = base_handler()
    elif type == 'LOCKS':
        res = lock_handler()
    elif type == 'BATCH':
        res = batch_handler()
    else:
        res = create_response(status_code=400)

    return res


def create_response(status_code=200, response=None):
    """Create the response according to the given parameters."""
    default_headers = {'Accept': "application/vnd.git-lfs+json",
                       'Content-Type': "application/vnd.git-lfs+json"}
    response = {'isBase64Encoded': False,
                'statusCode': status_code,
                'headers': default_headers}
    if response:
        response['body'] = str(response)
    return response


def batch_handler():
    """Handle batch requests."""


def base_handler():
    """Return the root of lfs repo."""
    return create_response()


def lock_handler():
    """Handle lock requests. Currently not supported."""
    return create_response(status_code=404)
