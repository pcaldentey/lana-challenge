"""
    Discount class is defined using strategy pattern.

    Discount object receives an strategy class in the moment is instantiated.
    We have two strtegy classes TwoPerOneDiscountStrategy and BulkDiscountStrategy
    both implement DiscountStrategy interface
"""
from abc import ABC
from abc import abstractmethod


class DiscountStrategy(ABC):
    """ Discount Strategy Interface class """

    @abstractmethod
    def apply_discount(self, items_number, price_per_item):
        pass


class Discount:
    """ Discount placeholder class """

    def __init__(self, discount_strategy: DiscountStrategy):
        self._discount_strategy = discount_strategy

    def apply_discount(self, product, items):
        """
            Applies discount :_discount_strategy:
            to :product:
        """
        return self._discount_strategy.apply_discount(items, product.price_per_unit)


# Concrete discount strategies

class TwoPerOneDiscountStrategy(DiscountStrategy):
    """ 2 per 1 Discount Strategy """
    def apply_discount(self, items, price_per_item):
        if items != 1:
            # How many groups of two element (items // 2) plus rest
            # Thats the number of 'items' times the price_per_item we have to charge
            times = (items // 2) + (items % 2)
            result = price_per_item * times
        else:
            result = price_per_item

        return result


class BulkDiscountStrategy(DiscountStrategy):
    """ Bulk Discount Strategy """
    def __init__(self, percent_discount, limit):
        super(BulkDiscountStrategy, self).__init__()
        self._percent_discount = percent_discount / float(100)
        self._limit = limit

    def apply_discount(self, items_number, price_per_item):
        if items_number >= self._limit:
            discounted_price = (1 - self._percent_discount) * price_per_item
            result = discounted_price * items_number
        else:
            result = price_per_item * items_number

        return result
