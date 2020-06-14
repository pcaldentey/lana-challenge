import json
import requests
import unittest


class TestGetBasketCheckoutEndpoint(unittest.TestCase):
    def setUp(self):
        self._server_url = 'http://0.0.0.0'

    def create_basket(self):
        data_dict = {}
        response = requests.post('{}/basket'.format(self._server_url), json=data_dict)
        data = json.loads(response.text)
        self.assertEqual(response.status_code, 201)
        return data['basket_id']

    def update_basket(self, basket_id, product_code, amount):
        data_dict = {
            "product_code": product_code,
            "amount": amount
        }
        requests.post('{}/basket/{}/product'.format(self._server_url, basket_id), json=data_dict)

    def test_checkout_unexisting_basket(self):
        response = requests.get('{}/basket/{}'.format(self._server_url, 25))
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.text)
        self.assertEqual(data['detail'], 'Basket not found')

    def test_checkout_empty_basket(self):
        basket_id = self.create_basket()

        expected = {'price': '0.0', 'items': []}

        response = requests.get('{}/basket/{}'.format(self._server_url, basket_id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data, expected)

    def test_checkout_basket_case_1(self):
        """
            Case 1
            Items: PEN, TSHIRT, MUG
            Total: 32.50€
        """
        basket_id = self.create_basket()
        self.update_basket(basket_id, 'PEN', 1)
        self.update_basket(basket_id, 'TSHIRT', 1)
        self.update_basket(basket_id, 'MUG', 1)
        expected = {'items': ['PEN', 'TSHIRT', 'MUG'], 'price': '32.5'}

        response = requests.get('{}/basket/{}'.format(self._server_url, basket_id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data, expected)

    def test_checkout_basket_case_2(self):
        """
             Case 2
             Items: PEN, TSHIRT, PEN
             Total: 25.00€
        """
        basket_id = self.create_basket()
        self.update_basket(basket_id, 'PEN', 2)
        self.update_basket(basket_id, 'TSHIRT', 1)

        expected = {'price': '25.0', 'items': ['PEN', 'PEN', 'TSHIRT']}

        response = requests.get('{}/basket/{}'.format(self._server_url, basket_id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data, expected)

    def test_checkout_basket_case_3(self):
        """
            Case 3
            Items: TSHIRT, TSHIRT, TSHIRT, PEN, TSHIRT
            Total: 65.00€
        """
        basket_id = self.create_basket()
        self.update_basket(basket_id, 'PEN', 1)
        self.update_basket(basket_id, 'TSHIRT', 4)

        expected = {'items': ['PEN', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT'], 'price': '65.0'}

        response = requests.get('{}/basket/{}'.format(self._server_url, basket_id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data, expected)

    def test_checkout_basket_case_4(self):
        """
            Case 4
            Items: PEN, TSHIRT, PEN, PEN, MUG, TSHIRT, TSHIRT
            Total: 62.50€
        """
        basket_id = self.create_basket()
        self.update_basket(basket_id, 'PEN', 3)
        self.update_basket(basket_id, 'TSHIRT', 3)
        self.update_basket(basket_id, 'MUG', 1)

        expected = {'items': ['PEN', 'PEN', 'PEN', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'MUG'], 'price': '62.5'}

        response = requests.get('{}/basket/{}'.format(self._server_url, basket_id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data, expected)
