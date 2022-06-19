"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contract_Groups(ApiBase):
    """Class for contract Groups APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTGROUP')
