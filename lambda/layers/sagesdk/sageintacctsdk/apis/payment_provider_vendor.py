"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class PaymentProviderVendor(ApiBase):
    """Class for Payment Provider Vendors APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROVIDERVENDOR')
