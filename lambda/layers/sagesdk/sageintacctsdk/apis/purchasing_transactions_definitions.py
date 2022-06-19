"""
Sage Intacct Expense Payment Types
"""
from typing import Dict

from .api_base import ApiBase


class PurchasingTransactionsDefinitions(ApiBase):
    """Class for Purchasing Transactios Definitions APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PODOCUMENTPARAMS')
