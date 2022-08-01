import time

from .base_page import BasePage

from elements import Elements
from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings
from tools import RandomTools
from tools import DataNames

from src import CheckoutStepOne
from src import CheckoutStepOnePageError

DATA = DataSettings.config_data()
RANDOM_NAME = RandomTools.RandomValue.get_random_name_from_dictionary(
    DataNames.get_list_names())


class CheckoutStepOnePage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CheckoutStepOnePage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)

    def check_displayed_checkout_info(self):
        self.elements.check_is_displayed(*CheckoutStepOne.CHECKOUT_INFO)

    def check_error_message(self):
        got_value = self.elements.check_is_displayed(
            *CheckoutStepOne.ERROR_MESSAGE, time=.1)
        assert got_value is False,\
            CheckoutStepOnePageError.WRONG_FILLED_FORM.value

    def check_cart_page(self):
        got_url = self.get_url()
        assert got_url == CheckoutStepOne.LINK_CART,\
            CheckoutStepOnePageError.WRONG_WEBPAGE.value

    def check_checkout_step_two_page(self):
        got_url = self.get_url()
        assert got_url == CheckoutStepOne.LINK_CHECKOUT_STEP_TWO, \
            CheckoutStepOnePageError.WRONG_WEBPAGE.value

    def click_cancel(self):
        self.elements.check_is_displayed(*CheckoutStepOne.CANCEL_BUTTON)
        self.elements.click(*CheckoutStepOne.CANCEL_BUTTON)

    def click_continue(self):
        self.elements.check_is_displayed(*CheckoutStepOne.CONTINUE_BUTTON)
        self.elements.click(*CheckoutStepOne.CONTINUE_BUTTON)

    def enter_first_name(self):
        self.check_absence_of_text(element=CheckoutStepOne.FIRST_NAME_FIELD,
                                   expected_text=CheckoutStepOne.EMPTY_FIELD)
        self.enter_value(value=RANDOM_NAME,
                         element=CheckoutStepOne.FIRST_NAME_FIELD)

    def enter_last_name(self):
        self.check_absence_of_text(element=CheckoutStepOne.LAST_NAME_FIELD,
                                   expected_text=CheckoutStepOne.EMPTY_FIELD)
        self.enter_value(value=RANDOM_NAME,
                         element=CheckoutStepOne.LAST_NAME_FIELD)

    def enter_postal_code(self):
        self.check_absence_of_text(element=CheckoutStepOne.POSTAL_CODE_FIELD,
                                   expected_text=CheckoutStepOne.EMPTY_FIELD)
        self.enter_value(value=RANDOM_NAME,
                         element=CheckoutStepOne.POSTAL_CODE_FIELD)
