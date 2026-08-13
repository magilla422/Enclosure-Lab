"""
Driver validation.

Ensures a Driver contains reasonable values before
analysis begins.
"""

from .driver import Driver


class DriverValidator:
    """
    Validates loudspeaker driver data.
    """

    @staticmethod
    def validate(driver: Driver) -> None:
        """
        Raises ValueError if invalid data is detected.
        """

        if driver.fs <= 0:
            raise ValueError("Fs must be greater than zero.")

        if driver.qts <= 0:
            raise ValueError("Qts must be greater than zero.")

        if driver.vas <= 0:
            raise ValueError("Vas must be greater than zero.")

        if driver.re <= 0:
            raise ValueError("Re must be greater than zero.")

        if driver.sd <= 0:
            raise ValueError("Sd must be greater than zero.")

        if driver.xmax <= 0:
            raise ValueError("Xmax must be greater than zero.")