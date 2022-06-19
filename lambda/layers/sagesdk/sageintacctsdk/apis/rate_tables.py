"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class RateTables(ApiBase):
    """Class for RateTables APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='RATETABLE')
