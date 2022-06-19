"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class TransactionAllocation(ApiBase):
    """Class for Transaction allocation APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ALLOCATION')
