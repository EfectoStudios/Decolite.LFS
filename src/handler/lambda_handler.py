"""Function invocation module."""
from src.handler.routes import get_path_request
from src.service.authentication import authenticate
from src.service.batch_request import BatchResponse, BatchRequest, BatchAction
from src.service.uri_generator import create_uri


def lfs_handler(event, context):
    """Handle git lfs requests sent through API Gateway."""
    if 'Authorization' not in event['headers']:
        return create_response(status_code=401)
    elif not authenticate(event['headers']['Authorization']):
        return create_response(status_code=401)

    path = event['path']
    owner, repo, type = get_path_request(path)

    if type == 'BASE':
        res = base_handler()
    elif type == 'LOCKS':
        res = lock_handler()
    elif type == 'BATCH':
        res = batch_handler(owner, repo, event['body'])
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


def base_handler():
    """Return the root of lfs repo."""
    return create_response()


def lock_handler():
    """Handle lock requests. Currently not supported."""
    return create_response(status_code=404)


def batch_handler(owner, repo, request):
    """Handle batch requests."""
    req = BatchRequest()
    req.set_data_from_JSON(request)
    operation = req.get_data()['operation']

    objects = req.get_objects()
    res_objects = []
    for obj in objects:
        uri = create_uri(owner, repo, obj.get_data()['oid'],
                         upload=operation == 'upload')
        act = BatchAction(href=uri, operation_type=operation)
        obj.add_action(act)
        res_objects.append(obj.get_data())

    batch_res = BatchResponse(objects=res_objects)
    json_body = str(batch_res)

    res = create_response(response=json_body)
    return res
