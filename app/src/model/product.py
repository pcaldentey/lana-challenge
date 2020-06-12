#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel


class Product(BaseModel):
    """ Product Model. """
    id: str
    description: str
    price_per_unit: int
    discount_to_apply: str
