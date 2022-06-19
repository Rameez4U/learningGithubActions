"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class EmployeeTypes(ApiBase):
    """Class for Employee Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EMPLOYEETYPE')
