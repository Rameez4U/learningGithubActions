"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class RevenueRecognitionSchedule(ApiBase):
    """Class for Revenue Recognition Schedule Tempelate APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='REVRECSCHEDULE')
