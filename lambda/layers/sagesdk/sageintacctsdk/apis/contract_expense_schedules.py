"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ContractExpenseSchedules(ApiBase):
    """Class for contract Expenses schedules APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTEXPENSESCHEDULE')
