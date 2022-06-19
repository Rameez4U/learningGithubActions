"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ApTerms(ApiBase):
    """Class for AP Terms APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APTERM')
