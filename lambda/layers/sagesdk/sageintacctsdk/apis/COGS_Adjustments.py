"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class COGSAdjustments(ApiBase):
    """Class for COGS Adjustments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='COGSCLOSEDJE')
