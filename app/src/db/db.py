#!/usr/bin/env python
# -*- coding: utf-8 -*-
CATALOG = {
        'PEN': {'description': 'Lana Pen', 'price': 500, 'currency': '€', 'discounts': ['2per1']},
        'TSHIRT': {'description': 'Lana T-Shirt', 'price': 2000, 'currency': '€', 'discounts': ['bulk25']},
        'MUG': {'description': 'Lana Coffee Mug', 'price': 750, 'currency': '€', 'discounts': None}
}

DISCOUNTS = {
        '2per1': {'description': '2 por 1', 'status': 'active'},
        'bulk25': {
            'description': 'Bulk discount 25%',
            'status': 'active',
            'percent': 25,
            'limit_items': 3,
            'discount_type': 'BULK'
        }
}
