"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contract_Types(ApiBase):
    """Class for Contract Types  APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTTYPE')
