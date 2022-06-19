"""
Sage Intacct Expense Payment Types
"""
from typing import Dict

from .api_base import ApiBase


class PurchasingTransactionsSubtotalTemplate(ApiBase):
    """Class for Purchasing Transactions Subtotal Template List APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='POSUBTOTALTEMPLATE')
