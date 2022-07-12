class BaseElement:

    @staticmethod
    def find_element(browser: object, locator: str, element: str):
        """Find the specified element."""
        return browser.find_element(locator, element)

    @staticmethod
    def find_elements(browser: object, locator: str, element: str):
        """Find the specified element."""
        return browser.find_elements(locator, element)
