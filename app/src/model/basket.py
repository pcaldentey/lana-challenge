#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Dict
from typing import Optional
from typing import Tuple

from src.model.product import Product


class Basket(BaseModel):
    """ Basket object.
        id: Basket id
        products: list of products and amount of items of each product
            products = {
                "prod_code": (ProdObj, 2),
                "prod_code2": (ProdObj2, 5)
            }
    """
    id: Optional[int] = None
    products: Optional[Dict[str, Tuple[Product, int]]] = {}

    def add_product(self, product: Product, amount: int = 1):
        if not isinstance(product, Product):
            raise TypeError("Must be Product instance")

        # Sum amount items to product bucket
        if product.id in self.products:
            self.products[product.id] = (product, self.products[product.id][1] + amount)

        # Create product bucket and add amount items
        else:
            self.products[product.id] = (product, amount)
