"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class InventoryTransactions(ApiBase):
    """Class for Inventory Transactions APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='INVDOCUMENT')
