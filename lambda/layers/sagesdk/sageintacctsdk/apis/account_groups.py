"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class AccountGroups(ApiBase):
    """Class for Account Groups APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLACCTGRP')
