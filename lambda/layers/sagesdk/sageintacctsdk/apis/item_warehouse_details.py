"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Item_Warehouse_details(ApiBase):
    """Class for Item Warehouse Details References APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ITEMWAREHOUSEINFO')
