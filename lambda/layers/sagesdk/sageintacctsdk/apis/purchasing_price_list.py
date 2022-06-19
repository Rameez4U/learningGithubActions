"""
Sage Intacct Expense Payment Types
"""
from typing import Dict

from .api_base import ApiBase


class PurchasingPriceList(ApiBase):
    """Class for Purchasing Price List APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='POPRICELIST')
