import ast


def parse_file(source_code):
    #  TODO parse the file..
    parsed = ast.parse(source_code)
    return parsed
