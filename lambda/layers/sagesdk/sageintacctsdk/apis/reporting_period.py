"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ReportingPeriod(ApiBase):
    """Class for Reporting Period APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='REPORTINGPERIOD')
