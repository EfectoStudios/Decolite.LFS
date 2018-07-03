"""Creates and sends batch API requests."""


class BatchConstants(object):
    """Constants defined in batch API."""

    OPERATION_TYPES = {'upload': 'upload',
                       'download': 'download'}
    """Operations allowed in batch API."""

    TRANSFER_TYPES = {'basic': 'basic'}
    """Transfer types supported by the API."""


class JSONWrapper(object):
    """json wrapper that handles local info as a python dictionary."""

    def __init__(self):
        """Initialize the wrapper with an empty dictionary."""
        self._data = {}

    def get_data(self):
        """Return the data saved in the local dict."""
        return self._data


class BatchAction(JSONWrapper):
    """Action for a given object in a batch response."""

    def __init__(self):
        """Initialize batch action with the given parameter."""
        JSONWrapper.__init__(self)
        self._data[BatchConstants.OPERATION_TYPES['download']] = None


class BatchObject(JSONWrapper):
    """Object definition for a batch request."""

    def __init__(self, isResponse=False):
        """Initialize batch object with the given parameters."""
        JSONWrapper.__init__(self)
        self._data['oid'] = None
        self._data['size'] = None

        if isResponse:
            self._data['actions'] = None


class BatchRequest(JSONWrapper):
    """this class models a batch request."""

    def __init__(self, transfers, operation, objects):
        """Create batch request with the given parameters."""
        JSONWrapper.__init__(self)
        self._data['transfers'] = transfers
        self._data['operation'] = operation
        self._data['objects'] = objects


class BatchResponse(JSONWrapper):
    """This class models a batch response."""

    def __init__(self, transfer, objects):
        """Create batch response with the given parameters."""
        JSONWrapper.__init__(self)
        self._data['transfer'] = transfer
        self._data['objects'] = objects
