"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class VendorTypes(ApiBase):
    """Class for Vendor Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='VENDTYPE')
