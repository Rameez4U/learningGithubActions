"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class CustomerTypes(ApiBase):
    """Class for Customer types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CUSTTYPE')
