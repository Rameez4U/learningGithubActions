"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class APAdjustment(ApiBase):
    """Class for Ap Adjustments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APADJUSTMENT')
