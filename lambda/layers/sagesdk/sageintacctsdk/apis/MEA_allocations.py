"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class MEA_Allocations(ApiBase):
    """Class for MEA Allocations APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTMEABUNDLE')
