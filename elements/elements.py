from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_element import BaseElement

from tools import Logger
from tools import ChecksBrowserSettings


class Elements:
    """
    The methods that use find_element().
    """

    def __init__(self, browser: object = None):
        # self.browser = ChecksBrowserSettings.checks_the_use_of_singleton(browser)
        self.browser = browser

    def check_is_displayed(self,
                           locator: str,
                           element: str,
                           time: int = 10) -> bool:
        """Wait specified time or while file will be displayed."""
        Logger().info(f"Check is displayed element: {element}.")
        self.browser.implicitly_wait(time)
        try:
            BaseElement.find_element(self.browser, locator, element).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def click(self, locator: str, element: str) -> None:
        """Click the specified element."""
        Logger().info(f"Click element: {element}.")
        BaseElement.find_element(self.browser, locator, element).click()

    def get_to_attribute(self,
                         locator: str,
                         element: str,
                         attribute) -> str:
        """Get the specified attribute."""
        return BaseElement.find_element(
            self.browser, locator, element).get_attribute(attribute)

    def get_text(self, locator: str, element: str) -> str:
        """Get the text from specified element."""
        Logger().info(f"Get text from element: {element}.")
        return BaseElement.find_element(
            self.browser, locator, element).text

    def wait_element_to_be_clickable(self,
                                     locator: str,
                                     element: str,
                                     time: int = 10) -> None:
        """Will wait the element specified amount of time."""
        Logger().info(f"Wait element to be clickable(Element: {element}).")
        value = BaseElement.find_element(self.browser, locator, element)
        WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(value))
