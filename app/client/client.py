import json
import requests


class LanaClient:
    def __init__(self, server_url: str = 'http://0.0.0.0'):
        self._server_url = server_url

    def create_basket(self):
        data_dict = {}
        response = requests.post('{}/basket'.format(self._server_url), json=data_dict)
        if response.status_code != 200:
            print(response.content)

    def delete_basket(self, basket_id: int):
        response = requests.delete('{}/basket/{}'.format(self._server_url, basket_id))
        data = json.loads(response.text)
        if data['data']:
            return data['data'][0]
        return None

    def add_element_to_basket(self, basket_id: int, product_code: str, items: int = 1):
        data_dict = {
            "product_code": product_code,
            "amount": items
        }
        response = requests.post('{}/basket/{}/product'.format(self._server_url, basket_id), json=data_dict)
        data = json.loads(response.text)
        if data['data']:
            return data['data'][0]
        return None

    def get_total_amount_basket(self, basket_id: int):
        response = requests.get('{}/basket/{}'.format(self._server_url, basket_id))
        data = json.loads(response.text)
        if data['data']:
            return data['data'][0]
        return None
