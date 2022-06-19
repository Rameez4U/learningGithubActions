"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ACHBankConfiguration(ApiBase):
    """Class for ACH Bank Configuration APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ACHBANK')
