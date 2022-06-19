"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class UsageData(ApiBase):
    """Class for Usage Data APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTUSAGE')
