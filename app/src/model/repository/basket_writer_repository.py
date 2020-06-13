import pickle
import os
import time

from abc import ABC
from abc import abstractmethod
from pathlib import Path

from src.model.basket import Basket
from src.exceptions import BasketFileNotFoundException


class BasketWriterRepository(ABC):

    @abstractmethod
    def save(
            self,
            basket: Basket,
            database: str,
    ) -> Basket:
        raise NotImplementedError()

    @abstractmethod
    def delete(
            self,
            id: int,
            database: str,
    ):
        raise NotImplementedError()


class FileBasketWriterRepository(BasketWriterRepository):

    def save(
            self,
            basket: Basket,
            database: str,
    ) -> Basket:

        # Previously existing basket
        if basket and basket.id:
            my_file = Path("/path/to/file")
            if my_file.is_file():
                # file exists
                pass
            pass
        # Basket creation
        else:
            # basket id will be actual time in milliseconds
            id = int(round(time.time() * 1000))
            # empty basket saved
            with open(database + str(id), 'wb') as basket_file:
                pickle.dump({}, basket_file)
                basket = Basket()
                basket.id = id
                basket.products = None
                return basket

    def delete(
            self,
            id: int,
            database: str,
    ):

        # We just have to remove the file
        basket_file = Path(database + str(id))
        if basket_file.is_file():
            os.remove(basket_file)
        else:
            raise BasketFileNotFoundException("Basket file {} not found".format(id))
