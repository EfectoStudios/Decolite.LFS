"""Function invocation module."""
from base64 import b64decode
from ..service.authentication import authenticate


def lfs_handler(event, context):
    """Handle git lfs requests sent through API Gateway."""
    # Response skeleton
    response = {'isBase64Encoded': False,
                'statusCode': 200,
                'headers': {
                    'Accept': "application/vnd.git-lfs+json",
                    'Content-Type': "application/vnd.git-lfs+json"
                    },
                'body': ''}

    print(event)
    # Check for the Authorization header
    if 'Authorization' not in event['headers']:
        response['statusCode'] = 401
    elif 'Basic ' not in event['headers']['Authorization']:
        response['statusCode'] = 401
    else:
        auth_str = event['headers']['Authorization'][6:]
        auth = b64decode(auth_str.encode()).decode().split(':')
        if not authenticate(auth[0], auth[1]):
            response['statusCode'] = 401
    return response
