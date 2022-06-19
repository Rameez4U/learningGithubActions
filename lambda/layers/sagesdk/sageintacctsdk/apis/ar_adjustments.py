"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ARAcdjustments(ApiBase):
    """Class for AR Adjustments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARADJUSTMENT')
