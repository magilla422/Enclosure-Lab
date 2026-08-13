"""
Enclosure Lab

driver.py

Defines the immutable Driver object used throughout the application.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Driver:
    """
    Represents a loudspeaker driver.

    The Driver class is a read-only container for the
    measured or manufacturer supplied Thiele/Small parameters
    and related driver information.

    All engineering calculations are performed by other
    components within Enclosure Lab.
    """

    manufacturer: str
    model: str

    fs: float          # Resonant Frequency (Hz)
    qts: float         # Total Q
    vas: float         # Equivalent Compliance Volume (Liters)

    re: float          # Voice Coil DC Resistance (Ohms)
    sd: float          # Cone Area (cm²)
    xmax: float        # One-way Linear Excursion (mm)