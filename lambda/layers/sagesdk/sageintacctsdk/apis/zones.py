"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Zones(ApiBase):
    """Class for Zones APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ZONE')
