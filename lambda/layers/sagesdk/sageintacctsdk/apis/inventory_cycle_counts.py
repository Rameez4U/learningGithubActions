"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class InventoryCycleCount(ApiBase):
    """Class for Inventory Cycle Count APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ICCYCLECOUNT')
