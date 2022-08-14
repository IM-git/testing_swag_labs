import time

from .base_page import BasePage

from elements import Elements
from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings
from tools import RandomTools
from tools import DataNames

from src import CheckoutStepTwo
from src import CheckoutStepTwoPageError

DATA = DataSettings.config_data()
RANDOM_NAME = RandomTools.RandomValue.get_random_name_from_dictionary(
    DataNames.get_list_names())


class CheckoutStepTwoPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CheckoutStepTwoPage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)

    def click_cancel_button(self):
        self.elements.check_is_displayed(*CheckoutStepTwo.CANCEL_BUTTON)
        self.elements.click(*CheckoutStepTwo.CANCEL_BUTTON)

    def click_finish_button(self):
        self.elements.check_is_displayed(*CheckoutStepTwo.FINISH_BUTTON)
        self.elements.click(*CheckoutStepTwo.FINISH_BUTTON)

    def check_checkout_inventory_page(self):
        got_url = self.get_url()
        assert got_url == CheckoutStepTwo.LINK_CHECKOUT_INVENTORY,\
            CheckoutStepTwoPageError.WRONG_WEBPAGE.value

    def check_checkout_complete_page(self):
        got_url = self.get_url()
        assert got_url == CheckoutStepTwo.LINK_CHECKOUT_COMPLETE,\
            CheckoutStepTwoPageError.WRONG_WEBPAGE.value

    def check_displayed_summary_info(self):
        self.elements.check_is_displayed(*CheckoutStepTwo.SUMMARY_INFO)
