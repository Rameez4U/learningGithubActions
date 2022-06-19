"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class Savings_Accounts(ApiBase):
    """Class for Savings Account APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SAVINGSACCOUNT')
