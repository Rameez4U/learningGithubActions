"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class StandardTasks(ApiBase):
    """Class for Standard Tasks APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='STANDARDTASK')
