"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class WarehouseGroup(ApiBase):
    """Class for Warehouse Groups APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='WAREHOUSEGROUP')
