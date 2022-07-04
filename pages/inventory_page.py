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

    def check_cart_page(self) -> None:
        got_url = self.get_url()
        assert got_url == Inventory.LINK_CLICK_SHOPPING_CART_CONTAINER,\
            InventoryPageError.WRONG_WEBPAGE.value

    def check_prices_by_ascending_sort_order(self) -> None:
        prices_list = self.get_list_with_values(
            Inventory.INVENTORY_ITEM_PRICES)
        value = ComparisonTools.compare_sequences_numbers_by_sort_order(
            prices_list)
        assert value is False, \
            InventoryPageError.WRONG_DESCENDING_SORT_ORDER.value

    def check_prices_by_descending_sort_order(self) -> None:
        prices_list = self.get_list_with_values(
            Inventory.INVENTORY_ITEM_PRICES)
        value = ComparisonTools.compare_sequences_numbers_by_sort_order(
            prices_list)
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

    def click_add_to_card(self) -> None:
        values = Inventory.ADD_SAUCE_LABS_PRODUCT_BUTTONS_LIST
        value = RandomTools.RandomValue.get_random_value_from_sequence(values)
        values.remove(value)
        self.check_value_cart(value[0], Inventory.ADD_STATE)
        self.elements.click(*value[0])
        self.check_value_cart(value[1], Inventory.REMOVE_STATE)

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

    def click_shopping_cart_container(self) -> None:
        self.elements.check_is_displayed(*Inventory.PRODUCT_SORT_CONTAINER)
        self.elements.click(*Inventory.PRODUCT_SORT_CONTAINER)

    def get_list_with_values(self, elements: list) -> list:
        list_with_values = []
        for element in elements:
            value = self.elements.get_text(*element)
            list_with_values.append(value)
        return list_with_values

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
