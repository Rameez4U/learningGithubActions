"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ProjectType(ApiBase):
    """Class for Project type APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROJECTTYPE')
