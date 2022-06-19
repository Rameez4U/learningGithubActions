"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class InventoryTransactionDefinition(ApiBase):
    """Class for Inventory Transaction Definition APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='INVDOCUMENTPARAMS')
