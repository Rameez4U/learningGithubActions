"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class PaymentProviderBankAccount(ApiBase):
    """Class for Payment Provider Bank Account APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROVIDERBANKACCOUNT')
