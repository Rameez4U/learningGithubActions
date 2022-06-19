"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ARSummaries(ApiBase):
    """Class for AR Summaries APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARINVOICEBATCH')
