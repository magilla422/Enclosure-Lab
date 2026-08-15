"""
Enclosure Lab

application.py

Defines the intended application for a loudspeaker project.
"""

from enum import Enum, auto


class Application(Enum):
    """Primary application of the loudspeaker."""

    HOME_AUDIO = auto()
    HOME_THEATER = auto()
    STUDIO_MONITOR = auto()

    PA = auto()
    LINE_ARRAY = auto()

    SUBWOOFER = auto()

    CAR_AUDIO = auto()

    PORTABLE = auto()

    OUTDOOR = auto()

    EXPERIMENTAL = auto()