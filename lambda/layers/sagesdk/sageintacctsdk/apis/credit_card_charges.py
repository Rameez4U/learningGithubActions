"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class CreditCardCharges(ApiBase):
    """Class for Credit Card Charges APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CREDITCARDFEE')
