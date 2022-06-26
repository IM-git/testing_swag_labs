import time

from selenium.common import NoSuchElementException

from .base_page import BasePage

from elements import Elements
from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings
from tools import RandomTools
from tools import ComparisonTools

from src import Inventory
from src import InventoryPageError

DATA = DataSettings.config_data()


class InventoryPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(InventoryPage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)

    def check_that_all_was_reset_to_cart_badge(self) -> None:
        state = self.elements.check_is_displayed(
            *Inventory.SHOPPING_CART_BADGE, time=1)
        assert state is False,\
            InventoryPageError.WRONG_AFTER_RESET_SHOPPING_CART_BADGE.value

    def check_prices_by_ascending_sort_order(self) -> None:
        prices_list = self.get_list_with_values(Inventory.INVENTORY_ITEM_PRICES)
        value = ComparisonTools.compare_sequences_numbers_by_sort_order(prices_list)
        assert value is False, \
            InventoryPageError.WRONG_DESCENDING_SORT_ORDER.value

    def check_prices_by_descending_sort_order(self) -> None:
        prices_list = self.get_list_with_values(Inventory.INVENTORY_ITEM_PRICES)
        value = ComparisonTools.compare_sequences_numbers_by_sort_order(prices_list)
        assert value is True, \
            InventoryPageError.WRONG_DESCENDING_SORT_ORDER.value

    def check_names_by_descending_sort_order(self) -> None:
        names_list = self.get_list_with_values(Inventory.INVENTORY_ITEM_NAMES)
        value = ComparisonTools.compare_sequences_names_sort_order(names_list)
        assert value is True, \
            InventoryPageError.WRONG_DESCENDING_SORT_ORDER.value

    def check_names_by_ascending_sort_order(self) -> None:
        name_list = self.get_list_with_values(Inventory.INVENTORY_ITEM_NAMES)
        value = ComparisonTools.compare_sequences_names_sort_order(name_list)
        assert value is False, \
            InventoryPageError.WRONG_DESCENDING_SORT_ORDER.value

    def check_shopping_cart_badge(self, clicks_made: int) -> None:
        """Check of the value in shopping cart badge."""
        cart_badge_value = self.get_shopping_cart_badge_value()
        assert clicks_made == cart_badge_value,\
            InventoryPageError.WRONG_QUANTITY_SHOPPING_CART_BADGE.value

    def check_value_cart(self, values, expected_state: str) -> None:
        """The value of the button."""
        state = self.elements.get_text(*values)
        assert state == expected_state,\
            InventoryPageError.WRONG_VALUE_OF_THE_STATE.value

    def check_value_buttons(self) -> None:
        values = Inventory.ADD_SAUCE_LABS_PRODUCT_BUTTONS_LIST
        for value in values:
            try:
                self.check_value_cart(value[1], Inventory.ADD_STATE)
            except NoSuchElementException:
                print(InventoryPageError.WRONG_VALUE_OF_THE_STATE.value)

    #   move the method to the base_page class
    #   change InventoryPageError.WRONG_VALUE_OF_THE_STATE by exception(tools/exceptions/.)
    def change_window(self, original_window: str) -> None:
        """Will change window in browser,
        if link will be open in the new tab."""
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break

    def click_button(self,
                     element: tuple,
                     expect_url: str,
                     error_message: str) -> None:
        self.elements.wait_element_to_be_clickable(*element)
        self.elements.click(*element)
        got_url = self.get_url()
        assert got_url == expect_url, error_message

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

    def click_add_to_card(self) -> None:
        values = Inventory.ADD_SAUCE_LABS_PRODUCT_BUTTONS_LIST
        value = RandomTools.RandomValue.get_random_value_from_sequence(values)
        values.remove(value)
        self.check_value_cart(value[0], Inventory.ADD_STATE)
        self.elements.click(*value[0])
        self.check_value_cart(value[1], Inventory.REMOVE_STATE)

    def click_close_menu_sidebar(self) -> None:
        self.elements.wait_element_to_be_clickable(*Inventory.MENU_SIDEBAR_CLOSE)
        self.click_sidebar(
            element=Inventory.MENU_SIDEBAR_CLOSE,
            attribute_value=Inventory.ARIA_HIDDEN_VALUE_IF_SIDEBAR_HIDDEN,
            error_message=InventoryPageError.SIDEBAR_IS_DISPLAYED.value)

    def click_menu_sidebar(self) -> None:
        self.click_sidebar(
            element=Inventory.MENU_SIDEBAR_BUTTON,
            attribute_value=Inventory.ARIA_HIDDEN_VALUE_IF_SIDEBAR_OPEN,
            error_message=InventoryPageError.SIDEBAR_NOT_DISPLAYED.value)

    def click_product_sort_container(self) -> None:
        self.click_button(
            element=Inventory.PRODUCT_SORT_CONTAINER,
            expect_url=Inventory.LINK,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_random_value_in_container(self) -> None:
        """
        Performing the random clicks on the value in container.
        Checking the correct sort order in prices or names
        (it related with type of the sort order).
        """
        element_number = RandomTools.RandomValue.get_random_number(
            0, len(Inventory.PRODUCT_SORT_BY)-1)
        Logger().info(f'Click on the product sort container.')
        self.elements.click(*Inventory.PRODUCT_SORT_BY[element_number])
        if element_number == 0:
            self.check_names_by_ascending_sort_order()
        elif element_number == 1:
            self.check_names_by_descending_sort_order()
        elif element_number == 2:
            self.check_prices_by_ascending_sort_order()
        elif element_number == 3:
            self.check_prices_by_descending_sort_order()

    def click_sidebar_all_items(self) -> None:
        self.click_button(
            element=Inventory.ALL_ITEMS_LINK,
            expect_url=Inventory.LINK,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_sidebar_about(self) -> None:
        self.click_button(
            element=Inventory.ABOUT_LINK,
            expect_url=Inventory.LINK_CLICK_ABOUT,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_sidebar_logout(self) -> None:
        self.click_button(
            element=Inventory.LOGOUT_LINK,
            expect_url=Inventory.LINK_CLICK_LOGOUT,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_sidebar_reset_app_state(self) -> None:
        self.click_button(
            element=Inventory.RESET_APP_STATE_LINK,
            expect_url=Inventory.LINK,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_twitter_link(self) -> None:
        self.click_social_link(
            element=Inventory.TWITTER_LINK,
            expect_url=Inventory.URL_TWITTER,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_facebook_link(self) -> None:
        self.click_social_link(
            element=Inventory.FACEBOOK_LINK,
            expect_url=Inventory.URL_FACEBOOK,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_linkedin_link(self) -> None:
        self.click_social_link(
            element=Inventory.LINKEDIN_LINK,
            expect_url=Inventory.URL_LINKEDIN,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_shopping_cart_container(self) -> None:
        self.elements.check_is_displayed(*Inventory.PRODUCT_SORT_CONTAINER)
        self.elements.click(*Inventory.PRODUCT_SORT_CONTAINER)

    def click_sidebar(self,
                      element: tuple,
                      attribute_value: str,
                      error_message: str) -> None:
        self.elements.check_is_displayed(*element)
        self.elements.click(*element)
        attribute = self.elements.get_to_attribute(
            *Inventory.MENU_SIDEBAR,
            Inventory.ATTRIBUTE_MENU_SIDEBAR_ARIA_HIDDEN)
        assert attribute == attribute_value, error_message

    def delete_all_in_shopping_cart_container(self):
        self.click_menu_sidebar()
        self.click_sidebar_reset_app_state()

    def get_list_with_values(self, elements: list) -> list:
        list_with_values = []
        for element in elements:
            value = self.elements.get_text(*element)
            list_with_values.append(value)
        return list_with_values

    def get_shopping_cart_badge_value(self) -> int:
        return int(self.elements.get_text(*Inventory.SHOPPING_CART_BADGE))

    def random_clicks_add_to_card(self) -> None:
        """
        Performed the random quantity clicks by 'add to cart'.
        Will performed click only one time same button.
        """
        number_of_add_to_cart = RandomTools.RandomValue.get_random_number(
            1, len(Inventory.ADD_SAUCE_LABS_PRODUCT_BUTTONS_LIST))
        Logger().info(f'Number of "add to cart": {number_of_add_to_cart}.')
        for _ in range(number_of_add_to_cart):
            self.click_add_to_card()
        self.check_shopping_cart_badge(number_of_add_to_cart)

