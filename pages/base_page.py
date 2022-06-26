import time

import requests

from elements import Elements
from elements import KeyboardActions
from elements import MouseActions

from src import GlobalErrorMessages
from src import StatusCodes
from src import Base

from tools import Logger
from tools import DataSettings
from tools import ChecksBrowserSettings

DATA = DataSettings.config_data()


class BasePage:
    """
    BasePage combines all main commands
    in the common class.
    """

    def __init__(self, browser: object = None, url: str = None):

        self.browser = ChecksBrowserSettings.checks_the_use_of_singleton(
            browser)
        self.url = url
        # self.elements = Elements(ChecksBrowserSettings.passing_browser_to_elements(browser))
        self.elements = None
        self.mouse_actions = None
        self.keyboard_actions = None

    def check_url(self) -> None:
        """Compares that specified url with the actual url."""
        Logger().info(f"Checks that specified url is: {self.url}.")
        assert self.url == self.get_url(), GlobalErrorMessages.WRONG_PAGE

    def check_status_code(self,
                          status: int = StatusCodes.OK.value) -> None:
        """Checking status code a webpage.
        Get two values:
            url webpage in str format,
            expected status code in int format.
        By default, we wait status code 200 - OK."""
        status_code_webpage: int = requests.get(url=self.url).status_code
        Logger().info(f"Checking the page status code: {status_code_webpage}.")
        assert status_code_webpage == status, \
            GlobalErrorMessages.WRONG_STATUS_CODE.value

    def enter_value(self, value: str, element) -> None:
        """
        Method enters value.
        Didn't add more info in Logger().info()
        because of use this method for enter login/password.
        """
        Logger().info(f"Enter the value in the '{element[1]}' field.")

        self.elements.click(*element)
        self.keyboard_actions.enter_text(value)

    def get_url(self) -> str:
        """Use for get current url."""
        return self.browser.current_url

    def open_page(self) -> None:
        """Open a webpage.
        Need to enter the url of the webpage.
        Using string argument."""
        Logger().info(f"Open page: {self.url}.")
        self.browser.get(self.url)
