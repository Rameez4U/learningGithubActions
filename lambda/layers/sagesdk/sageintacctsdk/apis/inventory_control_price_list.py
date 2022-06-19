"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class InventoryControlPriceList(ApiBase):
    """Class for Inventory Control Price List APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='INVPRICELIST')
