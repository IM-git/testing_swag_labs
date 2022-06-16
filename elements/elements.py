from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_element import BaseElement

from tools import Logger


class Elements:
    """
    The methods that use find_element().
    """
    @staticmethod
    def check_is_displayed(browser: object,
                           locator: str,
                           element: str,
                           time: int = 10) -> bool:
        """Wait specified time or while file will be displayed."""
        Logger().info(f"Check is displayed element: {element}.")
        browser.implicitly_wait(time)
        value = BaseElement.find_element(browser, locator, element).is_displayed()
        return value

    @staticmethod
    def click(browser: object, locator: str, element: str) -> None:
        """Click the specified element."""
        Logger().info(f"Click element: {element}.")
        BaseElement.find_element(browser, locator, element).click()

    @staticmethod
    def get_to_attribute(browser: object,
                         locator: str,
                         element: str,
                         attribute) -> str:
        """Get the specified attribute."""
        return BaseElement.find_element(
            browser, locator, element).get_attribute(attribute)

    @staticmethod
    def get_text(browser: object, locator: str, element: str) -> str:
        """Get the text from specified element."""
        Logger().info(f"Get text from element: {element}.")
        return BaseElement.find_element(
            browser, locator, element).text

    @staticmethod
    def wait_element_to_be_clickable(browser: object,
                                     locator: str,
                                     element: str,
                                     time: int = 10) -> None:
        """Will wait the element specified amount of time."""
        Logger().info(f"Wait element to be clickable(Element: {element}).")
        value = BaseElement.find_element(browser, locator, element)
        WebDriverWait(browser, time).until(EC.element_to_be_clickable(value))
