'''
py.test
'''
import unittest
import os
from ast_parse.parse.utils import get_files, parse_file


class _TestCase(unittest.TestCase):

    def setUp(self):
        self.code_base = get_files()


class TestGetFiles(_TestCase):

    def test_get_files(self):
        http_files = self.code_base.list_files('django/http')
        assert 'request.py' in http_files


class TestParseFiles(_TestCase):

    def test_parse(self):
        _file = self.code_base.get_file('django/http', 'request.py')
        parse_file(_file)
