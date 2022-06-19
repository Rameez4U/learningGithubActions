"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ExpenseAdjustments(ApiBase):
    """Class for Expense Adjustments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EXPENSEADJUSTMENTS')
