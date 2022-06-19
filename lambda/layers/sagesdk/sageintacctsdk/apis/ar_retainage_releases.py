"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Ar_Retainage_Releases(ApiBase):
    """Class for Ar Retainage Releases APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARRETAINAGERELEASE')
