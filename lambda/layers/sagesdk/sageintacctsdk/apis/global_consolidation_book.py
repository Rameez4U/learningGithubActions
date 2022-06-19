"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Global_Consolidation_Book(ApiBase):
    """Class for Global Consolidation Book APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GCBOOK')
