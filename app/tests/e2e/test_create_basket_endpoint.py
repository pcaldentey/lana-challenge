import json
import requests
import unittest


class TestCreateBasketEndpoint(unittest.TestCase):
    def setUp(self):
        self._server_url = 'http://0.0.0.0'

    def test_create_ok(self):
        data_dict = {}
        response = requests.post('{}/basket'.format(self._server_url), json=data_dict)
        # data = json.loads(response.text)
        self.assertEqual(response.status_code, 201)
