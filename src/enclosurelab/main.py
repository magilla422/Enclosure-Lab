from enclosurelab.driver import Driver
from enclosurelab.project import Project


def main() -> None:

    project = Project(
        name="Mini Column Array"
    )

    driver = Driver(
        manufacturer="Dayton Audio",
        model="ND65-4",
        fs=83.1,
        qts=0.42,
        vas=2.8,
        re=3.3,
        sd=31.0,
        xmax=4.0,
    )

    project.add_driver_definition(driver)

    print(project)


if __name__ == "__main__":
    main()