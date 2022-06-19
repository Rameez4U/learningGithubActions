"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class TaskResources(ApiBase):
    """Class for Task Resources APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='TASKRESOURCES')
