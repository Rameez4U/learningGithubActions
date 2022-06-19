"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ProductLines(ApiBase):
    """Class for Product Lines References APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PRODUCTLINE')
