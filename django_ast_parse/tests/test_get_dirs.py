import unittest
from django_ast_parse import get_files


class TestGetFiles(unittest.TestCase):

    def test_get_files(self):
        # Thats all for now..
        assert list(get_files()) > 100
