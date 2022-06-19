"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class Budget(ApiBase):
    """Class for Budget APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLBUDGETHEADER')
