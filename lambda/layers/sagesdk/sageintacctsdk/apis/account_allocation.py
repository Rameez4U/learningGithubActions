"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class AccountAllocation(ApiBase):
    """Class for Account allocation APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLACCTALLOCATION')
