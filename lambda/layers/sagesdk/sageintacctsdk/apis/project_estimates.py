"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Project_Estimates(ApiBase):
    """Class for Project Estimates APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PJESTIMATE')
