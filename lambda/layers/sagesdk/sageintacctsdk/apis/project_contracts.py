"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ProjectContracts(ApiBase):
    """Class for Project Contracts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROJECTCONTRACT')
