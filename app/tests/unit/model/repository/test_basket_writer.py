import os
import unittest

from src.config import BASKET_DB_PATH
from src.exceptions import BasketFileNotFoundException
from src.model.basket import Basket
from src.model.product import Product
from src.model.repository.basket_writer_repository import FileBasketWriterRepository


class TestBasketWriter(unittest.TestCase):

    def setUp(self):
        self._writer = FileBasketWriterRepository(BASKET_DB_PATH)

    def test_creates_basket(self):
        empty_basket = Basket()
        basket = self._writer.save(empty_basket)
        # File exists
        self.assertTrue(os.path.isfile(BASKET_DB_PATH + str(basket.id)))
        # Cleaning
        self._writer.delete(basket.id)

    def test_update_basket(self):
        # create basket
        empty_basket = Basket()
        basket = self._writer.save(empty_basket)
        basket_file_path = BASKET_DB_PATH + str(basket.id)
        # File exists
        self.assertTrue(os.path.isfile(basket_file_path))
        creation_size = os.path.getsize(basket_file_path)

        # Populate basket
        product = Product()
        product.id = "TEST"
        product.description = "Test product"
        product.price_per_unit = 15

        basket.add_product(product, 8)
        self._writer.save(basket)
        self.assertTrue(os.path.isfile(basket_file_path))
        update_size = os.path.getsize(basket_file_path)

        # Comparing file sizes after and before update
        self.assertTrue(creation_size < update_size)

    def test_delete_basket(self):
        empty_basket = Basket()
        basket = self._writer.save(empty_basket)
        basket_file_path = BASKET_DB_PATH + str(basket.id)
        # File exists
        self.assertTrue(os.path.isfile(basket_file_path))

        self._writer.delete(basket.id)
        # File doesn't exist anymore
        self.assertFalse(os.path.isfile(basket_file_path))

    def test_delete_basket_unexisting(self):
        with self.assertRaises(BasketFileNotFoundException):
            self._writer.delete(2)
