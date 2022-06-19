"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class OtherReceipts(ApiBase):
    """Class for Other Receipts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='OTHERRECEIPTS')
