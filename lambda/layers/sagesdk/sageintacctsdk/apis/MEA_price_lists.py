"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class MEA_Price_Lists(ApiBase):
    """Class for MEA Price Lists APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTMEAPRICELIST')
