from src.model.repository.basket_writer_repository import BasketWriterRepository


class DeleteBasketService:
    def __init__(self, writer_repository: BasketWriterRepository):
        self.__writer = writer_repository

    def execute(self, id: int):
        self.__writer.delete(id)
        return {"msg": "Basket {} deleted".format(id)}
