"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class StatisticalAccount(ApiBase):
    """Class for Statistical Account  APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='STATACCOUNT')
