"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ProjectStatuses(ApiBase):
    """Class for Project Statuses APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROJECTSTATUS')
