"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Timesheets(ApiBase):
    """Class for Timesheets APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='TIMESHEET')
