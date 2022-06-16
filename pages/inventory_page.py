from .base_page import BasePage

from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings
from tools import RandomTools

from src import Inventory
from src import InventoryPageError

DATA = DataSettings.config_data()


class InventoryPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(InventoryPage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)

    def check_shopping_cart_badge(self, clicks_made: int) -> None:
        cart_badge_value = self.get_shopping_cart_badge_value()
        assert clicks_made == cart_badge_value,\
            InventoryPageError.WRONG_QUANTITY_SHOPPING_CART_BADGE.value

    def click_button_in_sidebar(self,
                                element: tuple,
                                expect_url: str,
                                error_message: str) -> None:
        self.elements.wait_element_to_be_clickable(self.browser, *element)
        self.elements.click(self.browser, *element)
        got_url = self.get_url()
        assert got_url == expect_url, error_message

    def click_add_to_card(self) -> None:
        values = Inventory.SAUCE_LABS_PRODUCT_BUTTONS_LIST
        value = RandomTools.RandomValue.get_random_value_from_sequence(values)
        values.remove(value)
        self.elements.click(self.browser, *value)

    def click_sidebar_all_items(self) -> None:
        self.click_button_in_sidebar(
            element=Inventory.ALL_ITEMS_LINK,
            expect_url=Inventory.LINK,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_sidebar_about(self) -> None:
        self.click_button_in_sidebar(
            element=Inventory.ABOUT_LINK,
            expect_url=Inventory.LINK_CLICK_ABOUT,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_sidebar_logout(self) -> None:
        self.click_button_in_sidebar(
            element=Inventory.LOGOUT_LINK,
            expect_url=Inventory.LINK_CLICK_LOGOUT,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_sidebar_reset_app_state(self) -> None:
        self.click_button_in_sidebar(
            element=Inventory.RESET_APP_STATE_LINK,
            expect_url=Inventory.LINK,
            error_message=InventoryPageError.WRONG_WEBPAGE.value)

    def click_close_menu_sidebar(self) -> None:
        self.click_sidebar(
            element=Inventory.MENU_SIDEBAR_CLOSE,
            attribute_value=Inventory.ARIA_HIDDEN_VALUE_IF_SIDEBAR_HIDDEN,
            error_message=InventoryPageError.SIDEBAR_IS_DISPLAYED.value)

    def click_menu_sidebar(self) -> None:
        self.click_sidebar(
            element=Inventory.MENU_SIDEBAR_BUTTON,
            attribute_value=Inventory.ARIA_HIDDEN_VALUE_IF_SIDEBAR_OPEN,
            error_message=InventoryPageError.SIDEBAR_NOT_DISPLAYED.value)

    def click_sidebar(self,
                      element: tuple,
                      attribute_value: str,
                      error_message: str) -> None:
        self.elements.check_is_displayed(self.browser, *element)
        self.elements.click(self.browser, *element)
        attribute = self.elements.get_to_attribute(
            self.browser, *Inventory.MENU_SIDEBAR,
            Inventory.ATTRIBUTE_MENU_SIDEBAR_ARIA_HIDDEN)
        assert attribute == attribute_value, error_message

    def get_shopping_cart_badge_value(self) -> int:
        return int(self.elements.get_text(
            self.browser, *Inventory.SHOPPING_CART_BADGE))

    def random_clicks_add_to_card(self) -> None:
        number_of_add_to_cart = RandomTools.RandomValue.get_random_number(
            1, len(Inventory.SAUCE_LABS_PRODUCT_BUTTONS_LIST))
        Logger().info(f'Number of "add to cart": {number_of_add_to_cart}.')
        for _ in range(number_of_add_to_cart):
            self.click_add_to_card()
        self.check_shopping_cart_badge(number_of_add_to_cart)

