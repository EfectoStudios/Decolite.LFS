"""Unit tests for routing."""
import unittest
from src.handler import routes


class RoutesTest(unittest.TestCase):
    """Unit tests for routes."""

    def test_path_rrequest(self):
        """Test request parsing."""
        base = '/someone/holi.git/info/lfs/'
        batch = base + 'objects/batch'
        locks = base + 'locks'

        self.assertEqual(('someone/holi.git', 'BATCH'),
                         routes.get_path_request(batch))
        self.assertEqual(('someone/holi.git', 'LOCKS'),
                         routes.get_path_request(locks))
        self.assertEqual(('someone/holi.git', 'BASE'),
                         routes.get_path_request(base))
        self.assertEqual(('someone/holi.git', 'BAD_REQUEST'),
                         routes.get_path_request(base+'surely/not/valid'))
        self.assertEqual((None, 'BAD_REQUEST'),
                         routes.get_path_request('surely/not/valid'))
