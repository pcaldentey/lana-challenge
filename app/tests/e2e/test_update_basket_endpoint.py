import json
import requests
import unittest


class TestUpdateBasketEndpoint(unittest.TestCase):
    def setUp(self):
        self._server_url = 'http://0.0.0.0'

    def create_basket(self):
        data_dict = {}
        response = requests.post('{}/basket'.format(self._server_url), json=data_dict)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 201)
        return data['basket_id']

    def test_update_unexisting_basket(self):
        # update basket
        data_dict = {
            "product_code": "MUG",
            "amount": 1
        }
        response = requests.post('{}/basket/{}/product'.format(self._server_url, 25), json=data_dict)
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.text)
        self.assertEqual(data['detail'], 'Basket not found')

    def test_update_ok(self):
        # create basket
        basket_id = self.create_basket()

        # update basket
        data_dict = {
            "product_code": "MUG",
            "amount": 1
        }
        response = requests.post('{}/basket/{}/product'.format(self._server_url, basket_id), json=data_dict)
        data = json.loads(response.text)
        self.assertEqual(data['msg'], 'Lana Coffee Mug product: 1 items added')

    def test_update_non_existing_product(self):
        # create basket
        basket_id = self.create_basket()

        # update basket
        data_dict = {
            "product_code": "MUGAA",
            "amount": 21
        }
        response = requests.post('{}/basket/{}/product'.format(self._server_url, basket_id), json=data_dict)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['detail'], 'Product not found')

    def test_update_empty_product(self):
        # create basket
        basket_id = self.create_basket()

        expected = [{'loc': ['body', 'product', 'product_code'], 'msg': 'field required',
                     'type': 'value_error.missing'}]

        # update basket
        data_dict = {
        }
        response = requests.post('{}/basket/{}/product'.format(self._server_url, basket_id), json=data_dict)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['detail'], expected)
