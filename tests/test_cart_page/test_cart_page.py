import allure

import time

import pytest

from pages import InventoryPage

from src import Inventory
from src import InventoryPageError


@allure.feature("Cart page.")
@allure.link(url=Inventory.LINK, name='INVENTORY_PAGE_LINK')
class TestCartPage:
    pass
