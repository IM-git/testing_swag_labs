import allure

import time

import pytest

from pages import InventoryPage

from src import Inventory


@allure.feature("Inventory page.")
@allure.link(url=Inventory.LINK, name='INVENTORY_PAGE_LINK')
class TestInventoryPage:
    """
    Testing of the inventory page.
    """

    def test_open_inventory_page(self, browser):
        """
        Checking the opening of the inventory page.
        """
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        time.sleep(1)

    def test_open_menu_sidebar(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        time.sleep(1)
