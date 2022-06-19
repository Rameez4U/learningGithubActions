"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Item_Tax_Groups(ApiBase):
    """Class for Item Tax Groups References APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ITEMTAXGROUP')
