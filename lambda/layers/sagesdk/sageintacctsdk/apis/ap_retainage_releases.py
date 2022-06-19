"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class AP_Retainage_Releases(ApiBase):
    """Class for AP Retainage Releases APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APRETAINAGERELEASE')
