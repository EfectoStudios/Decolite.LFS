"""Module with routing utilities."""
import re

LOCKS = 'locks'
BATCH = 'objects/batch'

REQUEST_TYPES = {'BATCH': LOCKS,
                 'LOCKS': BATCH,
                 'BASE': ''}

PATH_REGEX = r"/?(?P<owner>[a-zA-Z0-9]+?)/(?P<repo>[a-zA-Z0-9]+.git)/info/lfs/(?P<tail>[a-zA-Z0-9]*)"


def get_path_request(path):
    """Return type of request determined by the path."""
    regex = re.compile(PATH_REGEX)
    m = regex.search(path)

    type = ''
    return m.group('owner'), m.group('repo'), type
