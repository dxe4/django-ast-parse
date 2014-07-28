'''
py.test
'''
import unittest
import os
from ast_parse.parse.utils import get_files, parse_file


class _TestCase(unittest.TestCase):

    def setUp(self):
        self.result = get_files()
        self.files = self.result['files']
        self.directory = self.result['dir']
        self.http_dir = os.path.join(self.directory, 'django/http')


class TestGetFiles(_TestCase):

    def test_get_files(self):
        assert 'requset.py' in self.files[self.http_dir]


class TestParseFiles(_TestCase):

    def test_parse(self):
        http_files = self.files[self.http_dir]
        result = parse_file()
        assert result
