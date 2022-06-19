"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contract_Lines(ApiBase):
    """Class for contract lines  APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTDETAIL')
