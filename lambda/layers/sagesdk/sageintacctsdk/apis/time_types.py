"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class TimeTypes(ApiBase):
    """Class for Time Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='TIMETYPE')
