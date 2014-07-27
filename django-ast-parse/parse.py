import os
import ast
from pprint import pprint


def django_src_dir():
    dir_a = os.getenv('PARSE_DIR')
    dir_b = os.path.join(os.getenv('HOME'), 'dev/django')
    directory = dir_a or dir_b
    return directory


def excluded(django_dir):
    return [os.path.join(django_dir, i) for i in ('tests', 'docs')]


def should_exclude(directory, excluded_dirs):
    try:
        next((i for i in excluded_dirs if directory.startswith(i)))
        return True
    except StopIteration:
        return False


def find_all(django_dir, excluded_dirs=None):
    if not excluded_dirs:
        excluded_dirs = []

    for root, dir_names, file_names in os.walk(django_dir):
        if should_exclude(root, excluded_dirs):
            continue

        for file_name in file_names:
            if file_name.endswith('.py'):
                yield os.path.join(root, file_name)


django_dir = django_src_dir()
excluded_dirs = excluded(django_dir)

files = find_all(django_dir, excluded_dirs=excluded_dirs)
pprint(list(files))
