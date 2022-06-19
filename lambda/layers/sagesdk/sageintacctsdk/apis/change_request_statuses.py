"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Change_Request_Statuses(ApiBase):
    """Class for Change Request Status APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CHANGEREQUESTSTATUS')
