import unittest
from unittest.mock import patch

from src.exceptions import ProductNotFoundException
from src.model.repository.product_reader_repository import DictionaryProductReaderRepository

@patch('src.model.repository.product_reader_repository.CATALOG', {'Test': {'description': 'Lana test', 'price': 5,
                                                                           'discounts': None}})
class TestProductReader(unittest.TestCase):

    def setUp(self):
        self._reader = DictionaryProductReaderRepository()

    def test_read_unexisting_product(self):
        with self.assertRaises(ProductNotFoundException):
            self._reader.get("ss")

    def test_read_product(self):
        product = self._reader.get("Test")
        self.assertEqual(product.id, 'Test')
        self.assertEqual(product.description, 'Lana test')
        self.assertEqual(product.price_per_unit, 5)
