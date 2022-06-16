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
        inventory_page.click_menu_sidebar()
        time.sleep(1)

    def test_close_menu_sidebar(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_menu_sidebar()
        inventory_page.click_close_menu_sidebar()
        time.sleep(1)

    def test_click_sidebar_all_items(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_menu_sidebar()
        inventory_page.click_sidebar_all_items()

    def test_click_sidebar_about(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_menu_sidebar()
        inventory_page.click_sidebar_about()

    def test_click_sidebar_logout(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_menu_sidebar()
        inventory_page.click_sidebar_logout()

    def test_click_sidebar_reset_app_state(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_menu_sidebar()
        inventory_page.click_sidebar_reset_app_state()

    def test_click_add_to_card(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.random_clicks_add_to_card()
        time.sleep(1)

