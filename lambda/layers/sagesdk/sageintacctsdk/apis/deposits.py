"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class Deposits(ApiBase):
    """Class for deposit APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='DEPOSIT')
