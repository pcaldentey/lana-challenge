import unittest
from unittest.mock import patch

from src.exceptions import DiscountNotFoundException
from src.model.discount import Discount
from src.model.discount import TwoPerOneDiscountStrategy
from src.model.discount import BulkDiscountStrategy
from src.model.repository.discount_reader_repository import DictionaryDiscountReaderRepository
fake_discounts = {
        '2per1': {'description': '2 por 1', 'status': 'active'},
        'bulk25': {
            'description': 'Bulk discount 25%',
            'status': 'active',
            'percent': 25,
            'limit_items': 3,
            'discount_type': 'BULK'
        }
}


@patch('src.model.repository.discount_reader_repository.DISCOUNTS', fake_discounts)
class TestProductReader(unittest.TestCase):

    def setUp(self):
        self._reader = DictionaryDiscountReaderRepository()

    def test_read_unexisting_discount(self):
        with self.assertRaises(DiscountNotFoundException):
            self._reader.get("ss")

    def test_read_2per1(self):
        discount = self._reader.get("2per1")
        self.assertTrue(isinstance(discount, Discount))
        self.assertTrue(isinstance(discount._discount_strategy, TwoPerOneDiscountStrategy))

    def test_read_bulk(self):
        discount = self._reader.get("bulk25")
        self.assertTrue(isinstance(discount, Discount))
        self.assertTrue(isinstance(discount._discount_strategy, BulkDiscountStrategy))
        self.assertEqual(discount._discount_strategy._percent_discount, 0.25)
        self.assertEqual(discount._discount_strategy._limit, 3)
