"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class OrderEntryTransactionSubtotalTempelate(ApiBase):
    """Class for Order entry Transaction subtotal Tempelate APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SOSUBTOTALTEMPLATE')
