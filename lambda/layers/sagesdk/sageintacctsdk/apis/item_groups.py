"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ItemGroups(ApiBase):
    """Class for Item Groups References APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ITEMGROUP')
