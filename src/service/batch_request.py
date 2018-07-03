"""Creates and sends batch API requests."""


class BatchConstants(object):
    """Constants defined in batch API."""

    OPERATION_TYPES = {'upload': 'upload',
                       'download': 'download'}
    """Operations allowed in batch API."""

    TRANSFER_TYPES = {'basic': 'basic'}
    """Transfer types supported by the API."""


class BatchRequest(object):
    """this class models a batch request."""

    def __init__(self, transfers, operation, objects):
        """Create batch request with the given parameters."""
        self.transfers = transfers
        self.operation = operation
        self.objects = objects


class BatchResponse(object):
    """This class models a batch response."""

    def __init__(self, transfer, objects):
        """Create batch response with the given parameters."""
        self.transfer = transfer
        self.objects = objects
