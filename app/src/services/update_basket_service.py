
from src.model.basket import Basket
from src.model.repository.basket_writer_repository import BasketWriterRepository
from src.model.repository.product_reader_repository import ProductReaderRepository
from src.config import BASKET_DB_PATH


class UpdateBasketService:
    def __init__(self, writer_repository: BasketWriterRepository, product_reader: ProductReaderRepository):
        self.__writer = writer_repository
        self.__reader = product_reader

    def execute(self, basket_id: int, product_code: str, amount: int):
        empty_basket = Basket()
        empty_basket.id = None
        empty_basket.products = None

        basket = self.__writer.save(empty_basket, BASKET_DB_PATH)
        return {"basket_id": basket.id}
