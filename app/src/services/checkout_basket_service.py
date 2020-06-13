from src.model.repository.basket_reader_repository import BasketReaderRepository
from src.model.repository.product_reader_repository import ProductReaderRepository


class CheckoutBasketService:
    def __init__(self,
                 basket_reader_repository: BasketReaderRepository,
                 product_reader_repository: ProductReaderRepository
                 ):
        self.__basket_reader_repository = basket_reader_repository
        self.__product_reader_repository = product_reader_repository

    def __output(self):
        pass

    def execute(self, basket_id: int):
        # product = self.__product_reader_repository.get(product_code)
        basket = self.__basket_reader_repository.get(basket_id)

        return {"basket_id": basket.id, 'msg': ' product: items added'}
