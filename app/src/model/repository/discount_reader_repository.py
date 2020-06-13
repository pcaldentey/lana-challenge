from abc import ABC
from abc import abstractmethod

from src.db.db import DISCOUNTS
from src.exceptions import DiscountNotFoundException
from src.model.discount import Discount
from src.model.discount import TwoPerOneDiscountStrategy
from src.model.discount import BulkDiscountStrategy


class DiscountReaderRepository(ABC):
    """ DiscountReaderRepository interface """

    @abstractmethod
    def get(
            self,
            discount_code: str,
            database: str = None,
    ) -> Discount:
        raise NotImplementedError()


class DictionaryDiscountReaderRepository(DiscountReaderRepository):

    def get(
            self,
            discount_code: str,
            database: str = None,
    ) -> Discount:
        """ Loads Discount and discount strategy objects from dictionar """

        # Read discount information from DISCOUNTS dictionary
        # "bulk25": {"description": "Bulk discount 25%", "status": "active", "percent": 25, "limit_items": 3}
        if discount_code in DISCOUNTS:
            # Here we decide the strategy we have to inject to Discount object
            # to be applied. By code or type
            if discount_code == '2per1':
                discount_strategy = TwoPerOneDiscountStrategy()
            elif DISCOUNTS[discount_code]['discount_type'] == 'BULK':
                discount_strategy = BulkDiscountStrategy(DISCOUNTS[discount_code]['percent'],
                                                         DISCOUNTS[discount_code]['limit_items'])
            return Discount(discount_strategy)
        else:
            raise DiscountNotFoundException("Discount with code: {} not found".format(discount_code))
