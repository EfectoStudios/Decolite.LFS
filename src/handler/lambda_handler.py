"""Function invocation module."""


def lfs_handler(event, context):
    """Handle git lfs requests sent through API Gateway."""
    return {'statusCode': 200,
            'headers': {},
            'body': ''}
