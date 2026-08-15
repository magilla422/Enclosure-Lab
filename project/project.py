aaaaaaaaaaaaaaa"""
Enclosure Lab

project.py

Defines the root Project object.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from enclosurelab.core import Entity
from enclosurelab.driver import Driver

from .design_brief import DesignBrief


@dataclass(slots=True)
class Project(Entity):
    """
    Root engineering object.

    A Project represents an entire loudspeaker design and owns
    all engineering data associated with it.
    """

    design_brief: DesignBrief = field(default_factory=DesignBrief)

    driver_definitions: list[Driver] = field(default_factory=list)

    def add_driver_definition(self, driver: Driver) -> None:
        """
        Adds a driver definition to the project.
        """

        if driver not in self.driver_definitions:
            self.driver_definitions.append(driver)
            self.touch()

    def remove_driver_definition(self, driver: Driver) -> None:
        """
        Removes a driver definition.
        """

        if driver in self.driver_definitions:
            self.driver_definitions.remove(driver)
            self.touch()

    @property
    def driver_count(self) -> int:
        """
        Returns the number of driver definitions.
        """

        return len(self.driver_definitions)

    def summary(self) -> str:
        """
        Returns a formatted summary of the project.
        """

        lines = [
            f"Project: {self.name}",
            "",
            f"Description: {self.description or 'None'}",
            "",
            f"Application: {self.design_brief.application.name}",
            "",
            f"Objectives ({len(self.design_brief.objectives)}):",
        ]

        if self.design_brief.objectives:
            for objective in self.design_brief.objectives:
                lines.append(f"  - {objective.name}")
        else:
            lines.append("  None")

        lines.extend(
            [
                "",
                f"Driver Definitions: {self.driver_count}",
            ]
        )

        return "\n".join(lines)