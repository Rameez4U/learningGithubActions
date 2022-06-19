"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Unit_Measure(ApiBase):
    """Class for Unit Measure APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='UOM')
