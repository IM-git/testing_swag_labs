import allure

import time

import pytest

from pages import InventoryPage, LoginPage

from src import Inventory, Login

from credential import Credential


@allure.feature("Inventory page.")
@allure.link(url=Inventory.LINK, name='INVENTORY_PAGE_LINK')
class TestInventoryPage:
    """
    Testing of the inventory page.
    """

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, Login.LINK)
        login_page.open_page()
        login_page.check_url()
        login_page.enter_login(Credential.LOGIN_STANDARD)
        login_page.enter_password(Credential.PASSWORD)
        login_page.click_login_button()

    def test_inventory(self, browser):
        """
        Check inventory.
        """
        inventory_page = InventoryPage(browser, Inventory.LINK)
        inventory_page.open_page()
        time.sleep(1)
