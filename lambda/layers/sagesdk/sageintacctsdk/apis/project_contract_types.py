"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Project_Contract_Types(ApiBase):
    """Class for Project Contract_types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROJECTCONTRACTTYPE')
