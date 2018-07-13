"""Module with routing utilities."""
import re

LOCKS = 'locks'
BATCH = 'objects/batch'

REQUEST_TYPES = {BATCH: 'BATCH',
                 LOCKS: 'LOCKS',
                 '': 'BASE'}

PATH_REGEX = r"/?(?P<repo>[a-zA-Z0-9/]+.git)/info/lfs/?(?P<tail>[a-zA-Z0-9/]*)"


def get_path_request(path):
    """Return type of request determined by the path."""
    regex = re.compile(PATH_REGEX)
    m = regex.search(path)
    if not m:
        return None, None, 'BAD_REQUEST'
    type = REQUEST_TYPES.get(m.group('tail'), 'BAD_REQUEST')
    return m.group('repo'), type
