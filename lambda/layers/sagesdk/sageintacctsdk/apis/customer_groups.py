"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class CustomerGroup(ApiBase):
    """Class for Customer Groups APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CUSTOMERGROUP')
