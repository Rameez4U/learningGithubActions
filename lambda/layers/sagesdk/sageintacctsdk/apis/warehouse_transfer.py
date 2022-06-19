"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class WarehouseTransfer(ApiBase):
    """Class for Warehouse Transfer APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ICTRANSFER')
