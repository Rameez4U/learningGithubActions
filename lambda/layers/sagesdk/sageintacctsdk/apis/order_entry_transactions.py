"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class OrderEntryTransactions(ApiBase):
    """Class for Order entry Transaction  APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SODOCUMENT')
