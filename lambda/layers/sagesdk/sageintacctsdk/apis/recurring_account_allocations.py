"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class RecurringAccountAllocation(ApiBase):
    """Class for Recurring Account allocation APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='RECURGLACCTALLOCATION')
