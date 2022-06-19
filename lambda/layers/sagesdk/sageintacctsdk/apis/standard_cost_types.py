"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class StandardCostType(ApiBase):
    """Class for Standard Cost Type APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='STANDARDCOSTTYPE')
