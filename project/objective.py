"""
Enclosure Lab

objective.py

Defines design objectives for a loudspeaker project.
"""

from enum import Enum, auto


class Objective(Enum):
    """Engineering objectives for a loudspeaker design."""

    DEEP_BASS = auto()
    HIGH_SPL = auto()
    FLAT_RESPONSE = auto()
    LOW_DISTORTION = auto()
    LOW_GROUP_DELAY = auto()

    SMALL_SIZE = auto()
    LIGHT_WEIGHT = auto()
    LOW_COST = auto()

    HIGH_EFFICIENCY = auto()
    HIGH_POWER_HANDLING = auto()

    EASY_TO_BUILD = auto()

    PORTABLE = auto()