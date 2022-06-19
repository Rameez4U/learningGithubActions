"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contract_Expenses(ApiBase):
    """Class for contract Expenses APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTEXPENSE')
