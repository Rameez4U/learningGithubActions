"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class BankInterestIncome(ApiBase):
    """Class for Bank Interest Income APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='BANKFEE')
