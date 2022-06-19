"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ARTerms(ApiBase):
    """Class for AR Terms APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARTERM')
