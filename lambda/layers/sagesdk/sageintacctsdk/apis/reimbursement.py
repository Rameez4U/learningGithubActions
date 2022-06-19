"""
Sage Intacct Expense Payment Types
"""
from typing import Dict

from .api_base import ApiBase


class Reimbursement(ApiBase):
    """Class for Reimbursement Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EPPAYMENT')
