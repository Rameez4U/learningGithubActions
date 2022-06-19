"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class VendorGroups(ApiBase):
    """Class for Vendor Groups APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='VENDORGROUP')
