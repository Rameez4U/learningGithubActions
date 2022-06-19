"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ContractExpenseTemplate(ApiBase):
    """Class for contract Expenses template APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTEXPENSETEMPLATE')
