"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class FundTransfer(ApiBase):
    """Class for Fund Transfer APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='FUNDSTRANSFER')
