"""
Enclosure Lab

Main application entry point.
"""

from enclosurelab.driver import Driver
from enclosurelab.project import Project
from enclosurelab.project.application import Application
from enclosurelab.project.objective import Objective


def main() -> None:

    project = Project(
        name="Mini Column Array",
        description="Portable compact line array using Dayton ND65 drivers.",
    )

    project.design_brief.application = Application.LINE_ARRAY

    project.design_brief.add_objective(Objective.HIGH_SPL)
    project.design_brief.add_objective(Objective.PORTABLE)
    project.design_brief.add_objective(Objective.LIGHT_WEIGHT)

    project.design_brief.requirements.max_height_mm = 1200
    project.design_brief.requirements.max_budget = 1000

    nd65 = Driver(
        manufacturer="Dayton Audio",
        model="ND65-4",
        fs=83.1,
        qts=0.42,
        vas=2.8,
        re=3.3,
        sd=31.0,
        xmax=4.0,
    )

    project.add_driver_definition(nd65)

    print(project.summary())


if __name__ == "__main__":
    main()