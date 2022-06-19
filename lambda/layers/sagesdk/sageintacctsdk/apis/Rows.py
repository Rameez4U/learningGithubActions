"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Rows(ApiBase):
    """Class for Rows APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ICROW')
