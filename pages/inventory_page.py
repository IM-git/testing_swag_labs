from .base_page import BasePage

from elements import MouseActions
from elements import KeyboardActions

from tools import Logger
from tools import DataSettings

DATA = DataSettings.config_data()


class InventoryPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(InventoryPage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)
