"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class InventoryTotalDetails(ApiBase):
    """Class for inventory total details APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='INVENTORYTOTALDETAIL')
