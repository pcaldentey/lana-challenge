from abc import ABC
from abc import abstractmethod

from src.db.db import CATALOG
from src.exceptions import ProductNotFoundException
from src.model.product import Product


class ProductReaderRepository(ABC):
    """ ProductReaderRepository interface """

    @abstractmethod
    def get(
            self,
            product_code: str,
            database: str = None,
    ) -> Product:
        raise NotImplementedError()


class DictionaryProductReaderRepository(ProductReaderRepository):

    def get(
            self,
            product_code: str,
            database: str = None,
    ) -> Product:

        # Read product from CATALOG dictionary
        # and product object hydrated and returned
        # 'PEN': {'description': 'Lana Pen', 'price': 500, 'currency': '€', 'discounts': None},
        if product_code in CATALOG:
            product = Product()
            product.id = product_code
            product.description = CATALOG[product_code]['description']
            product.price_per_unit = CATALOG[product_code]['price']
            product.discount_to_apply = CATALOG[product_code]['discounts']
            return product

        else:
            raise ProductNotFoundException("Product with code: {} not found".format(product_code))
