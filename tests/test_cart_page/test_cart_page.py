import allure

import time

import pytest

from pages import CartPage

from src import Cart
from src import CartPageError


@allure.feature("Cart page.")
@allure.link(url=Cart.LINK, name='CART_PAGE_LINK')
class TestCartPage:

    def test_open_cart_page(self, browser):
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.check_url()
        # cart_page.

    def test_compare_quantity_in_description_and_badge(self, browser):
        cart_page = CartPage(browser, Cart.LINK)
        cart_page.check_url()
        # cart_page.get_quantity_descriptions()
        """Перенести стандартные методы из инвентаря в базовый """
