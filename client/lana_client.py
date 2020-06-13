import json
import requests


class LanaClient:
    def __init__(self, server_url: str = 'http://0.0.0.0'):
        self._server_url = server_url

    def create_basket(self):
        data_dict = {}
        response = requests.post('{}/basket'.format(self._server_url), json=data_dict)
        data = json.loads(response.text)
        if response.status_code != 201:
            print(response.content)
        else:
            print("Basket created!")
            print("Basket identifier: {}".format(data['basket_id']))
            return data['basket_id']

    def delete_basket(self, basket_id: int):
        response = requests.delete('{}/basket/{}'.format(self._server_url, basket_id))
        data = json.loads(response.text)
        if response.status_code != 200:
            print(response.content)
        else:
            print(data['msg'])

    def add_element_to_basket(self, basket_id: int, product_code: str, items: int = 1):
        data_dict = {
            "product_code": product_code,
            "amount": items
        }
        response = requests.post('{}/basket/{}/product'.format(self._server_url, basket_id), json=data_dict)
        data = json.loads(response.text)
        print(data)

    def get_total_amount_basket(self, basket_id: int):
        response = requests.get('{}/basket/{}'.format(self._server_url, basket_id))
        data = json.loads(response.text)
        if response.status_code == 200:
            print("Items: {}".format(", ".join(data['items'])))
            print("Total: {} €".format(data['price']))
        else:
            print(data)
