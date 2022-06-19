"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Bin(ApiBase):
    """Class for Bin APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='BIN')
