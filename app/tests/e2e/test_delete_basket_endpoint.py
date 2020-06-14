import json
import requests
import unittest


class TestDeleteBasketEndpoint(unittest.TestCase):
    def setUp(self):
        self._server_url = 'http://0.0.0.0'

    def test_delete_unexisting_basket(self):
        response = requests.delete('{}/basket/{}'.format(self._server_url, 25))
        data = json.loads(response.text)
        self.assertEqual(data['detail'], 'Basket not found')
        self.assertEqual(response.status_code, 404)

    def test_delete_ok(self):
        data_dict = {}
        response = requests.post('{}/basket'.format(self._server_url), json=data_dict)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 201)
        basket_id = data['basket_id']

        response = requests.delete('{}/basket/{}'.format(self._server_url, basket_id))
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['msg'], 'Basket {} deleted'.format(basket_id))
