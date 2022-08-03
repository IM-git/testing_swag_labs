import time

from .base_page import BasePage

from elements import Elements
from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings
from tools import RandomTools
from tools import DataNames

from src import CheckoutComplete
from src import CheckoutCompletePageError

DATA = DataSettings.config_data()
RANDOM_NAME = RandomTools.RandomValue.get_random_name_from_dictionary(
    DataNames.get_list_names())


class CheckoutCompletePage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CheckoutCompletePage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)

    def check_displayed_pony_express_img(self):
        self.elements.check_is_displayed(*CheckoutComplete.PONY_EXPRESS_IMG)

    def check_inventory_page_url(self):
        got_url = self.get_url()
        assert got_url == CheckoutComplete.LINK_INVENTORY,\
            CheckoutCompletePageError.WRONG_WEBPAGE.value

    def click_back_home_button(self):
        self.elements.check_is_displayed(*CheckoutComplete.BACK_HOME_BUTTON)
        self.elements.click(*CheckoutComplete.BACK_HOME_BUTTON)
