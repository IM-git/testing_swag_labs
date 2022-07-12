import allure

import time

import pytest

from pages import CartPage
from pages import InventoryPage

from src import Cart


@allure.feature("Cart page.")
@allure.link(url=Cart.LINK, name='CART_PAGE_LINK')
class TestCartPage:

    def test_open_cart_page(self, browser):
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.open_page()
        cart_page.check_url()
        cart_page.check_checkout_button()
        time.sleep(1)

    def test_click_continue_shopping(self, browser):
        """
        Check performing correctness of click
        continue shopping button.
        """
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.open_page()
        cart_page.check_url()
        cart_page.check_checkout_button()
        cart_page.click_continue_shopping_button()

    def test_click_checkout_button(self, browser):
        """
        Check performing correctness of click
        checkout button.
        """
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.open_page()
        cart_page.check_url()
        cart_page.check_checkout_button()
        cart_page.click_checkout_button()

    def test_click_remove(self, browser):
        """
        Check: Add random quantity of the product
        in the shopping cart, after that delete
        (from remove button) all products in the cart page.
        """
        cart_page = CartPage(browser, Cart.LINK)
        InventoryPage(browser).random_clicks_add_to_card()
        cart_page.open_page()
        cart_page.check_url()
        cart_page.check_checkout_button()
        cart_page.click_remove_button()
        cart_page.check_that_all_was_reset_to_cart_badge()

    def test_compare_quantity_in_description_and_badge(self, browser):
        """
        Comparison of the number of descriptions and the cart badge.
        Two identical numbers are expected.
        """
        cart_page = CartPage(browser, Cart.LINK)
        InventoryPage(browser).random_clicks_add_to_card()
        cart_page.open_page()
        cart_page.check_url()
        cart_page.check_checkout_button()
        cart_page.compare_quantity_in_descriptions_and_badge()
        InventoryPage(browser).delete_all_in_shopping_cart_container()
