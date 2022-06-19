"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class RecurringInvoice(ApiBase):
    """Class for  Recurring Invoice APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARRECURINVOICE')
