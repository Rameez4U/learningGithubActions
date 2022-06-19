"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Change_Requests(ApiBase):
    """Class for Change Requests APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CHANGEREQUEST')
