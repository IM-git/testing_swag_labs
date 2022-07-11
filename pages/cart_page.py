import time

from selenium.common import NoSuchElementException

from .base_page import BasePage

from elements import Elements
from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings

from src import Cart
from src import CartPageError

DATA = DataSettings.config_data()


class CartPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CartPage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)

    def get_quantity_descriptions(self) -> None:
        got_elements_in_description = self.browser.find_elements(
            *Cart.CART_QUANTITY)
        quantity_elements_in_description = len(got_elements_in_description)
        quantity_value_from_badge = int(self.elements.get_text(
            *Cart.SHOPPING_CART_BADGE))
        assert quantity_elements_in_description == quantity_value_from_badge,\
            CartPageError.WRONG_QUANTITY.value

    def check_checkout_button(self) -> None:
        self.elements.check_is_displayed(*Cart.CHECKOUT_BUTTON)

    def click_checkout_button(self) -> None:
        self.click_button(element=Cart.CHECKOUT_BUTTON,
                          expect_url=Cart.LINK_CHECKOUT_STEP_ONE,
                          error_message=CartPageError.WRONG_WEBPAGE.value)
        self.elements.check_is_displayed(*Cart.TITLE_SPAN)
        self.check_header_title(Cart.CHECKOUT_STEP_ONE_TITLE)

    def click_continue_shopping_button(self) -> None:
        self.elements.check_is_displayed(*Cart.CONTINUE_SHOPPING_BUTTON)
        self.click_button(element=Cart.CONTINUE_SHOPPING_BUTTON,
                          expect_url=Cart.LINK_INVENTORY_PAGE,
                          error_message=CartPageError.WRONG_WEBPAGE.value)
        self.elements.check_is_displayed(*Cart.TITLE_SPAN)
        self.check_header_title(Cart.PRODUCTS)
