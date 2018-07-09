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

        self.assertEqual(('someone', 'holi.git', ''),
                         routes.get_path_request(batch))
        self.assertEqual(('someone', 'holi.git', ''),
                         routes.get_path_request(locks))
