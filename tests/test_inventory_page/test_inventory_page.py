import allure

import time

import pytest

from pages import InventoryPage

from src import Inventory
from src import InventoryPageError


@allure.feature("Inventory page.")
@allure.link(url=Inventory.LINK, name='INVENTORY_PAGE_LINK')
@pytest.mark.usefixtures("authorization")
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

    def test_open_menu_sidebar(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_menu_sidebar()

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
        * Performing deletion in this test.
        """
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.random_clicks_add_to_card()
        inventory_page.delete_all_in_shopping_cart_container()

    def test_click_chopping_cart_container(self, browser):
        """Perform click on the chopping cart icon."""
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_shopping_cart_container()

    def test_click_product_sort_container(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_shopping_cart_container()
        inventory_page.click_random_value_in_container()

    @pytest.mark.parametrize('element, expect_url', Inventory.PARAMETRIZE_SOCIAL)
    def test_social_link(self, browser, element, expect_url):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        #   need to find other realization, because it isn't pageobject.
        inventory_page.click_social_link(element, expect_url, InventoryPageError.WRONG_WEBPAGE.value)

    @pytest.mark.xfail(reason="In the progress to correction.")
    def test_close_menu_sidebar(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_menu_sidebar()
        inventory_page.click_close_menu_sidebar()

    @pytest.mark.xfail(reason="BUG! After click to a reset buttons value don't change.")
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

    def test_click_shopping_cart_link(self, browser):
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.check_url()
        inventory_page.click_shopping_cart_link()
        inventory_page.check_cart_page()
