"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class LaborClasses(ApiBase):
    """Class for Labor Classes APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='LABORCLASS')
