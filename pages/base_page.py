import time

import requests

from elements import Elements
from elements import KeyboardActions
from elements import MouseActions

from src import BasePageError
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

    def click_button(self,
                     element: tuple,
                     expect_url: str,
                     error_message: str) -> None:
        self.elements.wait_element_to_be_clickable(*element)
        self.elements.click(*element)
        got_url = self.get_url()
        assert got_url == expect_url, error_message

    def click_close_menu_sidebar(self) -> None:
        self.elements.wait_element_to_be_clickable(
            *Base.MENU_SIDEBAR_CLOSE)
        self.click_sidebar(
            element=Base.MENU_SIDEBAR_CLOSE,
            attribute_value=Base.ARIA_HIDDEN_VALUE_IF_SIDEBAR_HIDDEN,
            error_message=BasePageError.SIDEBAR_IS_DISPLAYED.value)

    def click_menu_sidebar(self) -> None:
        self.click_sidebar(
            element=Base.MENU_SIDEBAR_BUTTON,
            attribute_value=Base.ARIA_HIDDEN_VALUE_IF_SIDEBAR_OPEN,
            error_message=BasePageError.SIDEBAR_NOT_DISPLAYED.value)

    def click_sidebar(self,
                      element: tuple,
                      attribute_value: str,
                      error_message: str) -> None:
        self.elements.check_is_displayed(*element)
        self.elements.click(*element)
        attribute = self.elements.get_to_attribute(
            *Base.MENU_SIDEBAR,
            Base.ATTRIBUTE_MENU_SIDEBAR_ARIA_HIDDEN)
        assert attribute == attribute_value, error_message

    def click_sidebar_all_items(self) -> None:
        self.click_button(
            element=Base.ALL_ITEMS_LINK,
            expect_url=self.url,
            error_message=BasePageError.WRONG_WEBPAGE.value)

    #   Check how ill be work expect_url
    def click_sidebar_about(self) -> None:
        self.click_button(
            element=Base.ABOUT_LINK,
            expect_url=Base.LINK_CLICK_ABOUT,
            error_message=BasePageError.WRONG_WEBPAGE.value)

    def click_sidebar_logout(self) -> None:
        self.click_button(
            element=Base.LOGOUT_LINK,
            expect_url=Base.LINK,
            error_message=BasePageError.WRONG_WEBPAGE.value)

    def click_sidebar_reset_app_state(self) -> None:
        self.click_button(
            element=Base.RESET_APP_STATE_LINK,
            expect_url=self.get_url(),
            error_message=BasePageError.WRONG_WEBPAGE.value)

    def click_facebook_link(self) -> None:
        self.click_social_link(
            element=Base.FACEBOOK_LINK,
            expect_url=Base.URL_FACEBOOK,
            error_message=BasePageError.WRONG_WEBPAGE.value)

    def click_linkedin_link(self) -> None:
        self.click_social_link(
            element=Base.LINKEDIN_LINK,
            expect_url=Base.URL_LINKEDIN,
            error_message=BasePageError.WRONG_WEBPAGE.value)

    def click_twitter_link(self) -> None:
        self.click_social_link(
            element=Base.TWITTER_LINK,
            expect_url=Base.URL_TWITTER,
            error_message=BasePageError.WRONG_WEBPAGE.value)

    def click_shopping_cart_link(self) -> None:
        self.elements.check_is_displayed(*Base.SHOPPING_CART_LINK)
        self.elements.click(*Base.SHOPPING_CART_LINK)

    def click_social_link(self,
                          element: tuple,
                          expect_url: str,
                          error_message: str) -> None:
        self.elements.wait_element_to_be_clickable(*element)
        original_window = self.browser.current_window_handle
        self.elements.click(*element)
        self.change_window(original_window)
        got_url = self.get_url()
        self.browser.close()
        self.browser.switch_to.window(original_window)
        assert got_url == expect_url, error_message

    def check_text(self, element: tuple, expected_text: str) -> None:
        """Two text values are compared."""
        self.elements.check_is_displayed(*element)
        got_text = self.elements.get_text(*element).lower()
        assert got_text == expected_text, BasePageError.WRONG_TEXT.value

    def check_absence_of_text(self, element: tuple, expected_text: str) -> None:
        """Check that field is empty."""
        self.elements.check_is_displayed(*element)
        got_text = self.elements.get_text(*element).lower()
        assert got_text == expected_text, BasePageError.WRONG_TEXT.value

    def check_header_title(self, expected_text: str) -> None:
        """Checks header title on the page."""
        self.check_text(element=Base.TITLE_SPAN,
                        expected_text=expected_text)

    def check_that_all_was_reset_to_cart_badge(self) -> None:
        """Checking the absence of a shopping cart badge(Value=0)."""
        check_of_cart_badge = self.elements.check_is_displayed(
            *Base.SHOPPING_CART_BADGE, time=.1)
        assert check_of_cart_badge is False,\
            BasePageError.WRONG_AFTER_RESET_SHOPPING_CART_BADGE.value

    def check_url(self) -> None:
        """Compares that specified url with the actual url."""
        Logger().info(f"Checks that specified url is: {self.url}.")
        assert self.url == self.get_url(), BasePageError.WRONG_PAGE.value

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
            BasePageError.WRONG_STATUS_CODE.value

    #   move the method to the base_page class
    #   change InventoryPageError.WRONG_VALUE_OF_THE_STATE by exception(tools/exceptions/.)
    def change_window(self, original_window: str) -> None:
        """Will change window in browser,
        if link will be open in the new tab."""
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break

    def delete_all_in_shopping_cart_container(self):
        self.click_menu_sidebar()
        self.click_sidebar_reset_app_state()

    def enter_value(self, value: str, element) -> None:
        """
        Method enters value.
        Didn't add more info in Logger().info()
        because of use this method for enter login/password.
        """
        Logger().info(f"Enter the value in the '{element[1]}' field.")

        # self.elements.click(*element)
        self.mouse_actions.double_click(element)
        self.keyboard_actions.enter_text(value)

    def get_shopping_cart_badge_value(self) -> int:
        return int(self.elements.get_text(*Base.SHOPPING_CART_BADGE))

    def get_url(self) -> str:
        """Use for get current url."""
        return self.browser.current_url

    def open_page(self) -> None:
        """Open a webpage.
        Need to enter the url of the webpage.
        Using string argument."""
        Logger().info(f"Open page: {self.url}.")
        self.browser.get(self.url)
