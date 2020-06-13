from src.model.basket import Basket
from src.model.repository.basket_writer_repository import BasketWriterRepository


class CreateBasketService:
    def __init__(self, writer_repository: BasketWriterRepository):
        self.__writer = writer_repository

    def execute(self):
        empty_basket = Basket()
        empty_basket.id = None
        empty_basket.products = None

        basket = self.__writer.save(empty_basket)
        return {"basket_id": basket.id}
