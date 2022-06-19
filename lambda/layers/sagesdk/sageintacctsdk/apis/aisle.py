"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Aisle(ApiBase):
    """Class for Aisle APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='AISLE')
