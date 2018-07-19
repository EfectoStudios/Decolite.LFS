"""Creates and sends batch API requests."""


class BatchConstants(object):
    """Constants defined in batch API."""

    OPERATION_TYPES = {'upload': 'upload',
                       'download': 'download',
                       'verify': 'verify'}
    """Operations allowed in batch API."""

    TRANSFER_TYPES = {'basic': 'basic'}
    """Transfer types supported by the API."""


def create_batch_action(href, expires_in=300, header=None):
    """Create a batch response action."""
    action = {'href': href, 'expires_in': expires_in}
    if header:
        action['header'] = header
    return action


def create_batch_object(oid, size=0, upload=None, download=None,
                        verify=None, error=None, authenticated=False):
    """Create a batch object."""
    obj = {'oid': oid, 'size': size}
    if authenticated:
        obj['authenticated'] = True
    if error:
        obj['error'] = error

    actions = {}
    if upload:
        actions[BatchConstants.OPERATION_TYPES['upload']] = upload
    if download:
        actions[BatchConstants.OPERATION_TYPES['download']] = download
    if verify:
        actions[BatchConstants.OPERATION_TYPES['verify']] = verify

    obj['actions'] = actions
    return obj


def create_batch_request(transfers=[BatchConstants.TRANSFER_TYPES['basic']],
                         operation=BatchConstants.OPERATION_TYPES['upload'],
                         objects=None):
    """Create a batch request."""
    return {'transfers': transfers, 'operation': operation, 'objects': objects}


def create_batch_response(transfer=BatchConstants.TRANSFER_TYPES['basic'],
                          objects=[]):
    """Create a batch response."""
    return {'transfer': transfer, 'objects': objects}
