"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class InventoryWorkQueueDetails(ApiBase):
    """Class for Inventory Work Queue APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='INVENTORYWQDETAIL')
