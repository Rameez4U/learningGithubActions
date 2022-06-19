"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ApSummaries(ApiBase):
    """Class for AP Summaries APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APBILLBATCH')
