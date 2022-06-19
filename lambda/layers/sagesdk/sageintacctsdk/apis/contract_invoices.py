"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contract_Invoices(ApiBase):
    """Class for contract invoices  APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GENINVOICEPREVIEW')
