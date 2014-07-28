import os
from collections import defaultdict


def _django_src_dir():
    dir_a = os.getenv('PARSE_DIR')
    dir_b = os.path.join(os.getenv('HOME'), 'dev/django')
    directory = dir_a or dir_b
    return directory


def _excluded(django_dir):
    return [os.path.join(django_dir, i) for i in ('tests', 'docs')]


def _should_exclude(directory, excluded_dirs):
    try:
        next((i for i in excluded_dirs if directory.startswith(i)))
        return True
    except StopIteration:
        return False


def _find_all(django_dir, excluded_dirs=None):
    result = defaultdict(set)

    if not excluded_dirs:
        excluded_dirs = []

    for root, dir_names, file_names in os.walk(django_dir):
        if _should_exclude(root, excluded_dirs):
            continue

        for file_name in file_names:
            if file_name.endswith('.py'):
                result[root].add(file_name)
    result = {
        'files': result,
        'dir': django_dir
    }
    return result


def get_files(django_dir=None):
    '''
    Returns a generator of most .py files in the django codebase
    Excluded dirs are: [tests, docs]
    '''
    django_dir = django_dir or _django_src_dir()
    excluded_dirs = _excluded(django_dir)

    files = _find_all(django_dir, excluded_dirs=excluded_dirs)
    return files
