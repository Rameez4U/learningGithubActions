"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Consolidation_Override_Accounts(ApiBase):
    """Class for Consolidation Override Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GCBOOKACCTRATETYPE')
