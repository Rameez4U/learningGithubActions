"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class EmployeeGroups(ApiBase):
    """Class for Employee Groups APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EMPLOYEEGROUP')
