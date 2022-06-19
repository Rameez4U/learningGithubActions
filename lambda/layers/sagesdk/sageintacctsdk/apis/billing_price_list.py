"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class BillingPriceList(ApiBase):
    """Class for Billing Price List APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTPRICELIST')
