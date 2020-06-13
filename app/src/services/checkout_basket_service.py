from src.model.repository.basket_reader_repository import BasketReaderRepository
from src.model.repository.discount_reader_repository import DiscountReaderRepository
from src.model.basket import Basket


class CheckoutBasketService:
    def __init__(self,
                 basket_reader_repository: BasketReaderRepository,
                 discount_reader_repository: DiscountReaderRepository
                 ):
        self._basket_reader_repository = basket_reader_repository
        self._discount_reader_repository = discount_reader_repository

    def _output(self, basket: Basket, price: int):
        item_list = []

        # create a list of items product codes, one for each item in our basket
        for code, product_tuple in basket.products.items():
            product_amount = product_tuple[1]
            for i in range(product_amount):
                item_list.append(code)

        # formatting price to euros
        return {'price': '{}'.format(price/float(100)), 'items': item_list}

    def _calculate_basket_price(self, basket: Basket):
        total_price = 0

        for code, product_tuple in basket.products.items():
            product = product_tuple[0]
            product_amount = product_tuple[1]
            # Apply discount if any discount is configured for this product
            if product.discount_to_apply:
                try:
                    discount = self._discount_reader_repository.get(product.discount_to_apply)
                    price = discount.apply_discount(product, product_amount)
                except Exception as e:
                    print(e)
                    # In case of any problem when retreiving or applying discount, we will act as if no discount was
                    # configured for this product
                    price = product_amount * product.price_per_unit
            else:
                price = product_amount * product.price_per_unit

            total_price = total_price + price

        return total_price

    def execute(self, basket_id: int):
        basket = self._basket_reader_repository.get(basket_id)
        total_price = self ._calculate_basket_price(basket)

        return self._output(basket, total_price)
