
from src.model.basket import Basket
from src.model.repository.basket_writer_repository import BasketWriterRepository
from src.config import BASKET_DB_PATH


class CreateBasketService:
    def __init__(self, writer_repository: BasketWriterRepository):
        self.__writer = writer_repository

    def execute(self):
        empty_basket = Basket()
        empty_basket.id = None
        empty_basket.products = None

        basket = self.__writer.save(empty_basket, BASKET_DB_PATH)
        return {"basket_id": basket.id}
