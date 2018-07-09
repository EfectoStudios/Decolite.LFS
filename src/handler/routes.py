"""Module with routing utilities."""

LOCKS = 'locks'
BATCH = 'objects/batch'

REQUEST_TYPES = {'BATCH': LOCKS,
                 'LOCKS': BATCH,
                 'BASE': ''}

PATH_REGEX = r"/?(?P<owner>\\w+)/(?<repo>\\w+.git)/info/lfs/(?<tail>\\w*)"


def get_path_request(path):
    """Return type of request determined by the path."""
    pass
