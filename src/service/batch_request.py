"""Creates and sends batch API requests."""
import json


class BatchConstants(object):
    """Constants defined in batch API."""

    OPERATION_TYPES = {'upload': 'upload',
                       'download': 'download',
                       'verify': 'verify'}
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

    def set_data_from_JSON(self, json_string):
        """Set the wrapper data from a JSON string."""
        self._data = json.loads(json_string)

    def __str__(self):
        """Serialize the object as a JSON object."""
        return json.dumps(self._data)


class BatchAction(JSONWrapper):
    """Action for a given object in a batch response."""

    def __init__(self, href='', expires_in=300, header={},
                 operation_type=BatchConstants.OPERATION_TYPES['download']):
        """Initialize batch action with the given parameter."""
        JSONWrapper.__init__(self)
        action = {'href': href, 'expires_in': expires_in, 'header': header}
        self._data[operation_type] = action

    def set_data_from_JSON(self, json_string):
        """Set action content from json string."""
        temp = self._data.copy()
        super(BatchAction).set_data_from_JSON(json_string)
        # TODO terminar implementacion
        # verificar que mantiene la estructura de la accion


class BatchObject(JSONWrapper):
    """Object definition for a batch request."""

    def __init__(self, oid='', size=0, actions=[]):
        """Initialize batch object with the given parameters."""
        JSONWrapper.__init__(self)
        self._data['oid'] = oid
        self._data['size'] = size

        if len(actions) != 0:
            self._data['actions'] = actions

    def add_action(self, action):
        """Add a new action to the current object."""
        if 'actions' not in self._data.keys():
            self._data['actions'] = {}
        temp = action.get_data()
        self._data['actions'][list(temp.keys())[0]] = temp[list(temp.keys())[0]]  # noqa: E501


class BatchRequest(JSONWrapper):
    """this class models a batch request."""

    def __init__(self, operation=None, objects=[],
                 transfers=[BatchConstants.TRANSFER_TYPES['basic']]):
        """Create batch request with the given parameters."""
        JSONWrapper.__init__(self)
        self._data['transfers'] = transfers
        self._data['operation'] = operation
        self._data['objects'] = objects

    def get_objects(self):
        """Retrieve objects from data dictionary."""
        temp = self._data['objects']
        objects = []
        for o in temp:
            objects.append(BatchObject(oid=o['oid'], size=o['size']))
        return objects


class BatchResponse(JSONWrapper):
    """This class models a batch response."""

    def __init__(self, transfer=BatchConstants.TRANSFER_TYPES['basic'],
                 objects=[]):
        """Create batch response with the given parameters."""
        JSONWrapper.__init__(self)
        self._data['transfer'] = transfer
        self._data['objects'] = objects
