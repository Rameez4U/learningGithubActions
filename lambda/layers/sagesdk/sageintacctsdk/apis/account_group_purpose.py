"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class AccountGroupPurpose(ApiBase):
    """Class for Account group purpose APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLACCTGRPPURPOSE')
