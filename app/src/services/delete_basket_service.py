from src.model.repository.basket_writer_repository import BasketWriterRepository
from src.config import BASKET_DB_PATH


class DeleteBasketService:
    def __init__(self, writer_repository: BasketWriterRepository):
        self.__writer = writer_repository

    def execute(self, id: int):
        self.__writer.delete(id, BASKET_DB_PATH)
        return {"msg": "Basket {} deleted".format(id)}
