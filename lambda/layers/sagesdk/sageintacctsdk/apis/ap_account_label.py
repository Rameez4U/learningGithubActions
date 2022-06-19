"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class APAccountlabel(ApiBase):
    """Class for AP Account label APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APACCOUNTLABEL')
