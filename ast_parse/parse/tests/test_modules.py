import json
from django.test import TestCase, Client


class TestModules(TestCase):

    def setUp(self):
        self.client = Client()

    def test_all_modules_json(self):
        response = self.client.get('/modules/all/json')

        assert response.status_code == 200

        data = json.loads(response.content)
        files = data['files']
        from pprint import pprint
        pprint(files)
        assert len(files) > 50
        assert files[0].endswith('.py')
