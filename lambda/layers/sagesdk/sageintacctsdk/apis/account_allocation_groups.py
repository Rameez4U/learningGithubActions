"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class AccountsAllocationGroups(ApiBase):
    """Class for Account Allocation Groups APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLACCTALLOCATIONGRP')
