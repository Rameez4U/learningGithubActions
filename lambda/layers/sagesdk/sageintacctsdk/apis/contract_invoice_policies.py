"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contract_Invoice_Policies(ApiBase):
    """Class for contract invoice policies APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GENINVOICEPOLICY')
