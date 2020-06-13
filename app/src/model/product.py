#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel


class Product(BaseModel):
    """ Product Model. """
    id: str = None
    description: str = None
    price_per_unit: int = None
    discount_to_apply: str = None
