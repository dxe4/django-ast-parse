'''
py.test
'''
import unittest
from ast_parse.parse import get_files, parse_file


class TestGetFiles(unittest.TestCase):

    def test_get_files(self):
        # Thats all for now..
        assert len(list(get_files())) > 100


class TestParseFiles(unittest.TestCase):

    def test_parse(self):
        file_name = next(get_files())
        result = parse_file(file_name)
        assert result
