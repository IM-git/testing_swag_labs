from tools import DataSettings
from tools import WebDriver
from tools import InvalidConditionInTest

DATA = DataSettings.config_data()


class ChecksBrowserSettings:

    @staticmethod
    def checks_the_use_of_singleton(value):
        """
        Notice!
        The part of the constructor with if/elif/else statements
        is similar to the Browser.browser_() method, but the method
        browser_ is used to create a webdriver. The constructor checks
        the correctness of using the already created webdriver(browser)
        in the tests files.
        """
        if DATA["singleton"].lower() == "yes" and value is None:
            browser = WebDriver(DATA).driver
        elif DATA["singleton"].lower() == "no" and value is not None:
            browser = value
        else:
            raise InvalidConditionInTest
        return browser
