"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ConsolidationEntities(ApiBase):
    """Class for Consolidation Entities APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GCBOOKENTITY')
