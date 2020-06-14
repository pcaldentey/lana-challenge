import unittest
from src.model.basket import Basket
from src.model.product import Product


class TestBasket(unittest.TestCase):

    def test_initial_values(self):
        basket = Basket()
        self.assertIsNone(basket.id)
        self.assertEqual(basket.products, {})

    def test_add_product_object_wrong(self):
        with self.assertRaises(TypeError):
            basket = Basket()
            basket.id = 1
            basket.add_product(object())

    def test_add_product_object_ok(self):
        product = Product()
        product.id = "SOAP"
        basket = Basket()
        basket.id = 1
        basket.add_product(product)

        self.assertTrue(isinstance(basket.products['SOAP'][0], Product))
        self.assertTrue(isinstance(basket.products['SOAP'][1], int))
        self.assertEqual(basket.products['SOAP'][1], 1)
