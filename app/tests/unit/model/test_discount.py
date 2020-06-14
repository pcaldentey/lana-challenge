import unittest
from src.model.discount import Discount
from src.model.discount import DiscountStrategy
from src.model.discount import TwoPerOneDiscountStrategy
from src.model.discount import BulkDiscountStrategy
from src.model.product import Product


class FakeStrategy(DiscountStrategy):
    """ Fake strategy class """
    pass


class TestDiscount(unittest.TestCase):

    def test_discount_object_wrong(self):
        with self.assertRaises(TypeError):
            Discount(object())

    def test_incomplete_strategy_discount(self):
        with self.assertRaises(TypeError):
            FakeStrategy()

    def test_two_per_one_discount_strategy_discount_ok_via_discount_obj(self):
        price = 10
        strategy = TwoPerOneDiscountStrategy()
        discount = Discount(strategy)

        product = Product()
        product.id = "test"
        product.description = "test product"
        product.price_per_unit = price

        self.assertEqual(discount.apply_discount(product, 1), 10)
        self.assertEqual(discount.apply_discount(product, 2), 10)
        self.assertEqual(discount.apply_discount(product, 3), 20)
        self.assertEqual(discount.apply_discount(product, 4), 20)
        self.assertEqual(discount.apply_discount(product, 5), 30)
        self.assertEqual(discount.apply_discount(product, 6), 30)

    def test_two_per_one_discount_strategy_discount_ok(self):
        price = 10
        strategy = TwoPerOneDiscountStrategy()

        self.assertEqual(strategy.apply_discount(items=1, price_per_item=price), 10)
        self.assertEqual(strategy.apply_discount(items=2, price_per_item=price), 10)
        self.assertEqual(strategy.apply_discount(items=3, price_per_item=price), 20)
        self.assertEqual(strategy.apply_discount(items=4, price_per_item=price), 20)
        self.assertEqual(strategy.apply_discount(items=5, price_per_item=price), 30)
        self.assertEqual(strategy.apply_discount(items=6, price_per_item=price), 30)

    def test_bulk_discount_strategy_discount_ok(self):
        price = 10
        strategy = BulkDiscountStrategy(percent_discount=20, limit=3)

        self.assertEqual(strategy.apply_discount(items=1, price_per_item=price), 10)
        self.assertEqual(strategy.apply_discount(items=2, price_per_item=price), 20)
        self.assertEqual(strategy.apply_discount(items=3, price_per_item=price), 24)
        self.assertEqual(strategy.apply_discount(items=4, price_per_item=price), 32)
        self.assertEqual(strategy.apply_discount(items=5, price_per_item=price), 40)
        self.assertEqual(strategy.apply_discount(items=6, price_per_item=price), 48)
