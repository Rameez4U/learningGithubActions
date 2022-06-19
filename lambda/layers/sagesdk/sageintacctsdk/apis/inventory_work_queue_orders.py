"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class InventoryWorkQueueOrders(ApiBase):
    """Class for Inventory Work Orders APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='INVENTORYWQORDER')
