from selenium import webdriver
from .base_element import BaseElement


class MouseActions:
    """
    Here the common mouse actions.
    """

    def __init__(self, browser):
        self.__browser = browser
        self.__base_element = BaseElement()

    def move_to_element(self, element) -> None:
        """Moving the mouse to the middle of an element."""

        value = self.__base_element.find_element(self.__browser, *element)
        webdriver.ActionChains(self.__browser).\
            move_to_element(value).perform()

    def one_click(self, element) -> None:
        """One a click on the element."""

        value = self.__base_element.find_element(self.__browser, *element)
        webdriver.ActionChains(self.__browser).click(value).perform()

    def double_click(self, element) -> None:
        """Double the click on the element."""

        value = self.__base_element.find_element(self.__browser, *element)
        webdriver.ActionChains(
            self.__browser).double_click(value).perform()

    def right_click(self, element) -> None:
        """Right a click on the element."""

        value = self.__base_element.find_element(self.__browser, *element)
        webdriver.ActionChains(self.__browser).context_click(value).perform()

    def select_all_text(self, element) -> None:
        """Doing double clicks for select all text."""

        value = self.__base_element.find_element(self.__browser, *element)
        webdriver.ActionChains(
            self.__browser).double_click(value).click().perform()
