"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class RecurringBills(ApiBase):
    """Class for Recurring Bills APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APRECURBILL')
