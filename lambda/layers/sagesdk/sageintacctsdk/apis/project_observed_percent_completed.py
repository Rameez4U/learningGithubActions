"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Project_Observed_Percent_Completed(ApiBase):
    """Class for Project Observed Percent APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='OBSPCTCOMPLETED')
