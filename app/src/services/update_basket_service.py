from src.model.repository.basket_reader_repository import BasketReaderRepository
from src.model.repository.basket_writer_repository import BasketWriterRepository
from src.model.repository.product_reader_repository import ProductReaderRepository
from src.config import BASKET_DB_PATH


class UpdateBasketService:
    def __init__(self,
                 basket_writer_repository: BasketWriterRepository,
                 basket_reader_repository: BasketReaderRepository,
                 product_reader_repository: ProductReaderRepository
                 ):
        self.__basket_writer_repository = basket_writer_repository
        self.__basket_reader_repository = basket_reader_repository
        self.__product_reader_repository = product_reader_repository

    def execute(self, basket_id: int, product_code: str, amount: int):
        # product and basket objecs retrieve
        product = self.__product_reader_repository.get(product_code)
        basket = self.__basket_reader_repository.get(basket_id, BASKET_DB_PATH)

        basket.add_product(product, amount)

        # Save basket
        basket = self.__basket_writer_repository.save(basket, BASKET_DB_PATH)
        return {"basket_id": basket.id, 'msg': '{} product: {} items added'.format(product.description, amount)}
