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

    @pytest.mark.xfail(reason="In the progress to correction.")
    def test_close_menu_sidebar(self, browser):
        """
        * Need to find solution,
          how to wait some time for state
          while will the value change.
        """
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

    def test_clicks_add_to_card(self, browser):
        """
        Perform random quantity clicks
        on the different 'ADD TO CARD' and compare
        with quantity in the shopping cart badge.
        """
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.random_clicks_add_to_card()
        time.sleep(1)

    @pytest.mark.xfail(reason="After click to a reset buttons value don't change.")
    def test_to_operation_sidebar_reset_app_state(self, browser):
        """
        Perform random quantity clicks
        on the different 'ADD TO CARD',
        click 'RESET APP STATE',
        check value all buttons and cart badge.
        """
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.random_clicks_add_to_card()
        inventory_page.click_menu_sidebar()
        inventory_page.click_sidebar_reset_app_state()
        inventory_page.check_that_all_was_reset_to_cart_badge()
        inventory_page.check_value_buttons()
        time.sleep(1)
