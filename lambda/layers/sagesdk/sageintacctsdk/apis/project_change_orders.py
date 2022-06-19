"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ProjectChangeOrder(ApiBase):
    """Class for Project Change Order APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROJECTCHANGEORDER')
