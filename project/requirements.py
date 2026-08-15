"""
Enclosure Lab

requirements.py

Defines engineering requirements for a project.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Requirements:
    """Engineering requirements."""

    max_width_mm: float | None = None
    max_height_mm: float | None = None
    max_depth_mm: float | None = None

    max_weight_kg: float | None = None

    max_budget: float | None = None

    max_driver_count: int | None = None

    preferred_material: str | None = None