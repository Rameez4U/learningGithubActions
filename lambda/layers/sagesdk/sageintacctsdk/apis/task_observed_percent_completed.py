"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Task_Observed_Percent_Completed(ApiBase):
    """Class for Task Observed Percent Completed APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='OBSPCTCOMPLETED')
