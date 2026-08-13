"""
Enclosure Lab

Main application entry point.
"""

from enclosurelab.driver import Driver
from enclosurelab.driver.validator import DriverValidator


def main() -> None:
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

    DriverValidator.validate(driver)

    print(driver)


if __name__ == "__main__":
    main()