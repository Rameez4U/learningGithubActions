"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Project_Estimate_Types(ApiBase):
    """Class for Project Estimate Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PJESTIMATETYPE')
