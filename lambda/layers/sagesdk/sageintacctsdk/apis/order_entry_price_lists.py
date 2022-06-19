"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class OrderEntryPriceLists(ApiBase):
    """Class for Order entry Price Lists APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SOPRICELIST')
