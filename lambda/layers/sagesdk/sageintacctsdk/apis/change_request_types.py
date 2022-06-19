"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Change_Request_Types(ApiBase):
    """Class for Change Request Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CHANGEREQUESTTYPE')
