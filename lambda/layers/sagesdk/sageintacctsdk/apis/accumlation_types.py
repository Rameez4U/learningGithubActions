"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class AccumlationTypes(ApiBase):
    """Class for Accumlation Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ACCUMULATIONTYPE')
