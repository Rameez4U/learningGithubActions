"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Cost_Types(ApiBase):
    """Class for Cost Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='COSTTYPE')
