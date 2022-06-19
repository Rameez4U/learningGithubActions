"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ItemCrossReferences(ApiBase):
    """Class for Item Cross References APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ITEMCROSSREF')
