import allure

import time

import pytest

from pages import CheckoutCompletePage

from src import CheckoutComplete


@allure.feature("Checkout-Complete page.")
@allure.link(url=CheckoutComplete.LINK, name='CHECKOUT_COMPLETE_PAGE_LINK')
class TestCheckoutComplete:

    def test_open_checkout_complete_test(self, browser):
        """Fail. This webpage will be open without filling user bought-form."""
        checkout_complete = CheckoutCompletePage(browser, CheckoutComplete.LINK)
        checkout_complete.open_page()
        checkout_complete.check_url()
        checkout_complete.check_displayed_pony_express_img()
        time.sleep(1)

    def test_click_back_home(self, browser):
        checkout_complete = CheckoutCompletePage(browser, CheckoutComplete.LINK)
        checkout_complete.open_page()
        checkout_complete.check_url()

        checkout_complete.check_displayed_pony_express_img()
        checkout_complete.click_back_home_button()
        checkout_complete.check_inventory_page_url()
        time.sleep(1)
