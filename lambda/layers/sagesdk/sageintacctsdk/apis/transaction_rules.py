"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class TransactionRules(ApiBase):
    """Class for Transaction Rules APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='TRANSACTIONRULE')
