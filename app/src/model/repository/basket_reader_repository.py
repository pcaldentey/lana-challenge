import pickle

from abc import ABC
from abc import abstractmethod
from pathlib import Path

from src.model.basket import Basket
from src.exceptions import BasketFileNotFoundException


class BasketReaderRepository(ABC):
    """ BasketReaderRepository interface """

    @abstractmethod
    def get(
            self,
            basket_id: int,
    ) -> Basket:
        raise NotImplementedError()


class FileBasketReaderRepository(BasketReaderRepository):
    def __init__(self, database):
        self.__database = database

    def get(
            self,
            basket_id: int,
    ) -> Basket:
        """
            Basket obj is unserialized and returned
        """
        file_path = Path(self.__database + str(basket_id))
        if file_path.is_file():
            with open(file_path, 'rb') as basket_file:
                content = pickle.load(basket_file)
                basket = Basket()
                basket.id = basket_id
                basket.products = content
                return basket
        else:
            raise BasketFileNotFoundException("Basket file {} not found".format(basket_id))
