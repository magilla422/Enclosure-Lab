"""
Enclosure Lab

project.py

Defines the root Project object.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from enclosurelab.core import Entity
from enclosurelab.driver import Driver


@dataclass(slots=True)
class Project(Entity):
    """
    Root engineering object.

    A Project owns every component associated
    with a loudspeaker design.
    """

    driver_definitions: list[Driver] = field(default_factory=list)

    def add_driver_definition(self, driver: Driver) -> None:
        """
        Adds a driver definition to the project.
        """

        self.driver_definitions.append(driver)

        self.touch()