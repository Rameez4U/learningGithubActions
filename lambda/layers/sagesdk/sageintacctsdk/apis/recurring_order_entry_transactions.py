"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class RecurringOrderEntryTransactions(ApiBase):
    """Class for Recurring Order entry Transactions APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SORECURDOCUMENT')
