"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class PositionSkill(ApiBase):
    """Class for Position Skill APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='POSITIONSKILL')
