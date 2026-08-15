"""
Enclosure Lab

design_brief.py

Defines the engineering design brief for a project.
"""

from dataclasses import dataclass, field

from .application import Application
from .objective import Objective
from .requirements import Requirements


@dataclass(slots=True)
class DesignBrief:
    """
    Engineering design brief.

    Describes what the project is trying to accomplish.
    """

    application: Application = Application.HOME_AUDIO

    objectives: list[Objective] = field(default_factory=list)

    requirements: Requirements = field(default_factory=Requirements)

    notes: str = ""

    def add_objective(self, objective: Objective) -> None:
        """Adds an objective if it is not already present."""

        if objective not in self.objectives:
            self.objectives.append(objective)
           