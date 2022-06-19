"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ChargePayoff(ApiBase):
    """Class for Charge Payoff APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CHARGEPAYOFF')
