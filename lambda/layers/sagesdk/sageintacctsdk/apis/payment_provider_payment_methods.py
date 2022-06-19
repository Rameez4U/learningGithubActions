"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class PaymentProviderPaymentMethods(ApiBase):
    """Class for Payment Provider Payment Methods APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROVIDERPAYMENTMETHOD')
