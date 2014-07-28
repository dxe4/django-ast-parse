import json
from django.test import TestCase, Client


class TestModules(TestCase):

    def setUp(self):
        self.client = Client()

    # def test_all_files(self):
    #     response = self.client.get('/modules/all/json')

    #     assert response.status_code == 200

    #     data = json.loads(response.content)
    #     files = data['files']
    #     for _dir, _files in files.items():
    #         for _file in _files:
    #             assert _file.endswith('.py')

    #     assert len(files.keys()) > 10

    def test_all_modules(self):
        response = self.client.get('/modules/all/json')
        assert response.status_code == 200
        modules = json.loads(response.content)['modules']

        assert "/django/http" in modules
        assert len(modules) > 10
