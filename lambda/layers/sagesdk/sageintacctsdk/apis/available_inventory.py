"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class AvailableInventory(ApiBase):
    """Class for Available Inventory APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='AVAILABLEINVENTORY')
