"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class BankFeeds(ApiBase):
    """Class for Bank Feeds APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='BANKACCTTXNFEED')
