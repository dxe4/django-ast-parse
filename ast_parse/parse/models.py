import os


class NotFound(Exception):
    pass


class DjangoCodeBase(object):

    def __init__(self, codebase_dir, file_dict):
        self.codebase_dir = codebase_dir
        self.file_dict = {k.replace(codebase_dir, ''): v
                          for k, v in file_dict.items() if v}
        self.sub_dirs = self.file_dict.keys()

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

        # We should never really reach this point
        raise IOError('The file ({}) was found but something went'
                      ' wrong while reading it'.format(_file))

    def list_files(self, directory):
        if not directory.startswith("/"):
            directory = "/{}".format(directory)
        # directory = os.path.join(self.codebase_dir, directory)
        try:
            return self.file_dict[directory]
        except KeyError:
            raise NotFound('Directory {} not found'.format(directory))
