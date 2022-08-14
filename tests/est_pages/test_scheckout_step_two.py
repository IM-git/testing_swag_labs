import allure

import time

import pytest

from pages import CheckoutStepTwoPage

from src import CheckoutStepTwo


@allure.feature("Checkout-Step-One page.")
@allure.link(url=CheckoutStepTwo.LINK, name='CHECKOUT_STEP_ONE_PAGE_LINK')
class TestCheckoutStepTwo:

    def test_open_checkout_step_two_page(self, browser):
        """Fail. This webpage will be open without filling user bought-form."""
        checkout_step_two = CheckoutStepTwoPage(browser, CheckoutStepTwo.LINK)
        checkout_step_two.open_page()
        checkout_step_two.check_url()
        checkout_step_two.check_displayed_summary_info()
        time.sleep(1)

    def test_click_cancel(self, browser):
        checkout_step_two = CheckoutStepTwoPage(browser, CheckoutStepTwo.LINK)
        checkout_step_two.open_page()
        checkout_step_two.check_url()
        checkout_step_two.check_displayed_summary_info()
        checkout_step_two.click_cancel_button()
        checkout_step_two.check_checkout_inventory_page()

    def test_click_finish(self, browser):
        checkout_step_two = CheckoutStepTwoPage(browser, CheckoutStepTwo.LINK)
        checkout_step_two.open_page()
        checkout_step_two.check_url()
        checkout_step_two.check_displayed_summary_info()
        checkout_step_two.click_finish_button()
        checkout_step_two.check_checkout_complete_page()
