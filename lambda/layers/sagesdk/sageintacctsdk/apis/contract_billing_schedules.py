"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class ContractBillingSchedules(ApiBase):
    """Class for contract billing schedules APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTBILLINGSCHEDULE')
