#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel
from product import Product
from typing import Dict
from typing import Tuple


class Basket(BaseModel):
    """ Basket object.
        id: Basket id
        products: list of products and amount of items of each product
            products = {
                "prod_code": (ProdObj, 2),
                "prod_code2": (ProdObj2, 5)
            }
    """
    id: int
    products: Dict[str, Tuple(Product, int)]
