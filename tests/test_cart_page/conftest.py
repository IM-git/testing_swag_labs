import pytest
from pages import LoginPage
from pages import InventoryPage
from pages import CartPage
from src import Login
from src import Cart
from src import Inventory
from settings import LOGIN_STANDARD, PASSWORD


@pytest.fixture(scope="function", autouse=True)
def authorization(browser):
    LoginPage(browser, Login.LINK).authorization(LOGIN_STANDARD, PASSWORD)


@pytest.fixture(scope="function", autouse=True)
def open_cart_page(browser):
    InventoryPage(browser).random_clicks_add_to_card()
    CartPage(browser, Cart.LINK).open_page()
