"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ProjectGroup(ApiBase):
    """Class for Project Group APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROJECTGROUP')
