from patterns import Factory

from tools.test_settings.singleton_methods import WebDriver
from tools import InvalidConfigCondition


class Browser:

    @staticmethod
    def browser_(data):
        """Two options, create webdriver with singleton
        or without one.
        Condition pointed in the SINGLETON variable."""

        if data["singleton"].lower() == "no":
            driver = Factory().get_browser(data)  # without singleton
        elif data["singleton"].lower() == "yes":
            driver = WebDriver(data).driver     # singleton
        else:
            raise InvalidConfigCondition(data["singleton"])
        return driver
