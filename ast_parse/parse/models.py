import os


class NotFound(Exception):
    pass


class DjangoCodeBase(object):

    def __init__(self, codebase_dir, file_dict):
        self.codebase_dir = codebase_dir
        self.file_dict = file_dict
        self.sub_dirs = [i.replace(codebase_dir, '')
                         for i in file_dict.keys()]

    def get_file(self, directory, file_name, read=True):
        '''
        Returns: File path if read=False
        Returns: Source code of the file if read=True
        '''
        if not file_name.endswith('.py'):
            raise ValueError('File {} does not end with .py'.format(file_name))

        _file = os.path.join(self.codebase_dir, directory, file_name)
        if not read:
            return _file

        with open(_file, 'r') as f:
            return f.read()

    def list_files(self, directory):
        directory = os.path.join(self.codebase_dir, directory)
        return self.file_dict[directory]
