"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contracts(ApiBase):
    """Class for contracts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACT')
