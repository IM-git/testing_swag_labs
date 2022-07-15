import allure

import time

import pytest

from pages import CheckoutStepOnePage

from src import CheckoutStepOne


@allure.feature("Checkout-Step-One page.")
@allure.link(url=CheckoutStepOne.LINK, name='CHECKOUT_STEP_ONE_PAGE_LINK')
class TestCheckoutStepOne:

    def test_open_checkout_step_one_page(self, browser):
        checkout_step_one = CheckoutStepOnePage(browser, CheckoutStepOne.LINK)
        checkout_step_one.open_page()
        checkout_step_one.check_url()
        time.sleep(1)
