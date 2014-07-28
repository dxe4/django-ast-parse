'''
py.test
'''
import unittest
import os
from ast_parse.parse.utils import get_files, parse_file


class TestGetFiles(unittest.TestCase):

    def test_get_files(self):
        # Thats all for now..
        result = get_files()
        files = result['files']
        directory = result['dir']
        http_dir = os.path.join(directory, 'django/http')

        assert 'requset.py' in files[http_dir]


class TestParseFiles(unittest.TestCase):

    def test_parse(self):
        file_name = next(get_files())
        result = parse_file(file_name)
        assert result
