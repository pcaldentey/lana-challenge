import pickle

from abc import ABC
from abc import abstractmethod
from pathlib import Path

from src.model.basket import Basket
from src.exceptions import BasketFileNotFoundException


class BasketReaderRepository(ABC):

    @abstractmethod
    def get(
            self,
            basket_id: int,
            database: str,
    ) -> Basket:
        raise NotImplementedError()


class FileBasketReaderRepository(BasketReaderRepository):

    def get(
            self,
            basket_id: int,
            database: str,
    ) -> Basket:
        """
            Basket obj is unserialized and returned
        """
        file_path = Path(database + str(basket_id))
        if file_path.is_file():
            with open(file_path, 'rb') as basket_file:
                content = pickle.load(basket_file)
                basket = Basket()
                basket.id = basket_id
                basket.products = content
                return basket
        else:
            raise BasketFileNotFoundException("Basket file {} not found".format(basket_id))
