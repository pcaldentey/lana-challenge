import unittest

from src.config import BASKET_DB_PATH
from src.exceptions import BasketFileNotFoundException
from src.model.basket import Basket
from src.model.product import Product
from src.model.repository.basket_reader_repository import FileBasketReaderRepository
from src.model.repository.basket_writer_repository import FileBasketWriterRepository


class TestBasketReader(unittest.TestCase):

    def setUp(self):
        self._writer = FileBasketWriterRepository(BASKET_DB_PATH)
        self._reader = FileBasketReaderRepository(BASKET_DB_PATH)

    def test_read_unexisting_basket(self):
        with self.assertRaises(BasketFileNotFoundException):
            self._reader.get(14)

    def test_read_basket(self):
        # create basket
        empty_basket = Basket()
        basket = self._writer.save(empty_basket)

        # Populate basket
        product = Product()
        product.id = "TEST"
        product.description = "Test product"
        product.price_per_unit = 15

        basket.add_product(product, 8)
        self._writer.save(basket)

        retreived_basket = self._reader.get(basket.id)
        self.assertEqual(retreived_basket.id, basket.id)
        self.assertEqual(retreived_basket.products, basket.products)
