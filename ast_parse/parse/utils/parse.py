import ast
from ast_parse.parse.util import get_files


def parse_file(file_name):
    with open(file_name, 'r') as f:
        parsed = ast.parse(f.read())
        return parsed

    raise IOError('Error parsing {}'.format(file_name))
