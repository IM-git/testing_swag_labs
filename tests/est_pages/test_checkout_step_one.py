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
        checkout_step_one.check_displayed_checkout_info()
        time.sleep(1)

    def test_filling_out_form(self, browser):
        checkout_step_one = CheckoutStepOnePage(browser, CheckoutStepOne.LINK)
        checkout_step_one.open_page()
        checkout_step_one.check_url()
        checkout_step_one.check_displayed_checkout_info()
        checkout_step_one.enter_first_name()
        checkout_step_one.enter_last_name()
        checkout_step_one.enter_postal_code()

    def test_cancel_button(self, browser):
        checkout_step_one = CheckoutStepOnePage(browser, CheckoutStepOne.LINK)
        checkout_step_one.open_page()
        checkout_step_one.check_url()
        checkout_step_one.check_displayed_checkout_info()
        checkout_step_one.click_cancel()
        checkout_step_one.check_cart_page()

    def test_continue_button(self, browser):
        checkout_step_one = CheckoutStepOnePage(browser, CheckoutStepOne.LINK)
        checkout_step_one.open_page()
        checkout_step_one.check_url()
        checkout_step_one.check_displayed_checkout_info()
        checkout_step_one.enter_first_name()
        checkout_step_one.enter_last_name()
        checkout_step_one.enter_postal_code()
        checkout_step_one.click_continue()
        checkout_step_one.check_checkout_step_two_page()
