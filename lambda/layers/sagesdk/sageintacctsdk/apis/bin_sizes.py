"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class BinSizes(ApiBase):
    """Class for Bin Sizes APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='BINSIZE')
