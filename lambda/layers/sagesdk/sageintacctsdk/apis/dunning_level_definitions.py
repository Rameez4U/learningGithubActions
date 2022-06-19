"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class DunningLevelDefinition(ApiBase):
    """Class for Dunning Level Definition APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='DUNNINGDEFINITION')
