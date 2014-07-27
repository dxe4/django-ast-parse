import unittest
from django_ast_parse import get_files


class TestGetFiles(unittest.TestCase):

    def test_shuffle(self):
        assert list(get_files()) > 100
