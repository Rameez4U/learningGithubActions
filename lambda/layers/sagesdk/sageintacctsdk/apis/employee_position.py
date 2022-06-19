"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class EmployeePosition(ApiBase):
    """Class for Employee Position APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EMPLOYEEPOSITION')
