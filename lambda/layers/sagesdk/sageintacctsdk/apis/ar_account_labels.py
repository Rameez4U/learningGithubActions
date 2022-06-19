"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class ARAccountLabels(ApiBase):
    """Class for AR Account Labels APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARACCOUNTLABEL')
