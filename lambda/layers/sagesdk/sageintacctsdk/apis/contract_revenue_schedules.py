"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Contract_Revenue_Schedules(ApiBase):
    """Class for contract Revenue Schedule  APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTREVENUESCHEDULE')
