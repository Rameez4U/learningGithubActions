"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Warehouses(ApiBase):
    """Class for Warehouses APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='WAREHOUSE')
