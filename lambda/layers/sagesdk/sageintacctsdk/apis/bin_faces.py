"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class BinFaces(ApiBase):
    """Class for Bin Faces APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='BINFACE')
