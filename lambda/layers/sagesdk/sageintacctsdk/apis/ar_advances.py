"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ARAdvances(ApiBase):
    """Class for AR Advances APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARADVANCE')
