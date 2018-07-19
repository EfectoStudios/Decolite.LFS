"""Function invocation module."""
import json
from src.handler.routes import get_path_request
from src.service.authentication import authenticate
from src.service.batch_request import BatchConstants, create_batch_action,\
                                      create_batch_object, create_batch_response  # noqa: E501
from src.service.uri_generator import create_uri, file_exists


def lfs_handler(event, context):
    """Handle git lfs requests sent through API Gateway."""
    if not event['headers']:
        return create_response(status_code=401)
    elif 'Authorization' not in event['headers']:
        return create_response(status_code=401)
    elif not authenticate(event['headers']['Authorization']):
        return create_response(status_code=401)

    path = event['path']
    repo, type = get_path_request(path)

    if type == 'BASE':
        res = base_handler()
    elif type == 'LOCKS':
        res = lock_handler()
    elif type == 'BATCH':
        res = batch_handler(repo, event['body'])
    else:
        res = create_response(status_code=502)
    return res


def create_response(status_code=200, response=None):
    """Create the response according to the given parameters."""
    default_headers = {'Accept': "application/vnd.git-lfs+json",
                       'Content-Type': "application/vnd.git-lfs+json"}
    resp = {'isBase64Encoded': False,
            'statusCode': status_code,
            'headers': default_headers}
    if response:
        resp['body'] = str(response)
        print(str(response))
    return resp


def base_handler():
    """Return the root of lfs repo."""
    return create_response()


def lock_handler():
    """Handle lock requests. Currently not supported."""
    return create_response(status_code=404)


def batch_handler(repo, request):
    """Handle batch requests."""
    req = {}
    try:
        req = json.loads(request)
    except json.JSONDecodeError:
        return create_response(status_code=400)

    operation = req['operation']

    objects = req['objects']
    res_objects = []
    for obj in objects:
        down = None
        up = None
        err = None
        if file_exists(repo, obj['oid']):
            if operation == BatchConstants.OPERATION_TYPES['download']:
                uri = create_uri(repo, obj['oid'])
                down = create_batch_action(uri)
        else:
            if operation == BatchConstants.OPERATION_TYPES['upload']:
                uri = create_uri(repo, obj['oid'], upload=True)
                up = create_batch_action(uri)
            else:
                err = {'code': 404, 'message': 'File not found'}

        if down or up or err:
            res_objects.append(create_batch_object(obj['oid'], size=obj['size'],  # noqa: E501
                                                   upload=up, download=down,
                                                   error=err, authenticated=True))  # noqa: E501
    resp = create_batch_response(objects=res_objects)

    return create_response(response=json.dumps(resp))
