"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Consolidation_Elimination_Accounts(ApiBase):
    """Class for Consolidation Elimination Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GCBOOKELIMACCOUNT')
