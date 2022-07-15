import time

from .base_page import BasePage

from elements import Elements
from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings

from src import CheckoutStepOne
from src import CheckoutStepOnePageError

DATA = DataSettings.config_data()


class CheckoutStepOnePage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CheckoutStepOnePage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)
