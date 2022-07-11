import allure

import time

import pytest

from pages import CartPage

from src import Cart


@allure.feature("Cart page.")
@allure.link(url=Cart.LINK, name='CART_PAGE_LINK')
class TestCartPage:

    def test_open_cart_page(self, browser):
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.check_url()
        cart_page.check_checkout_button()

    def test_click_continue_shopping(self, browser):
        """
        Check performing correctness of click
        continue shopping button.
        """
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.check_url()
        cart_page.check_checkout_button()
        cart_page.click_continue_shopping_button()

    def test_click_checkout_button(self, browser):
        """
        Check performing correctness of click
        checkout button.
        """
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.check_url()
        cart_page.check_checkout_button()
        cart_page.click_checkout_button()

    @pytest.mark.xfail(reason="Need to be figure it out. Related with conftest.py")
    def test_compare_quantity_in_description_and_badge(self, browser):
        """
        Comparison of the number of descriptions and the cart badge.
        Two identical numbers are expected.
        """
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.check_url()
        cart_page.check_checkout_button()
        cart_page.get_quantity_descriptions()
