"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class EarningType(ApiBase):
    """Class for Earning Type APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EARNINGTYPE')
