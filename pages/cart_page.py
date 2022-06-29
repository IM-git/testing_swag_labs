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


class CartPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CartPage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)
