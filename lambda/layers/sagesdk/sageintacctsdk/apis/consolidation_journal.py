"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ConsolidationJournal(ApiBase):
    """Class for Consolidation Journal APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GCBOOKADJJOURNAL')
