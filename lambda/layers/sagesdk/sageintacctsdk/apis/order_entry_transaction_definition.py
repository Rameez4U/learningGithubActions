"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class OrderEntryTransactionDefinition(ApiBase):
    """Class for Order entry Transaction definitions APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SODOCUMENTPARAMS')
