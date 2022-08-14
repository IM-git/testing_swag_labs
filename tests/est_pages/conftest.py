import pytest
from pages import LoginPage
from pages import InventoryPage
from src import Login
from settings import LOGIN_STANDARD, PASSWORD


@pytest.fixture(scope="function", autouse=True)
def authorization(browser):
    LoginPage(browser, Login.LINK).authorization(LOGIN_STANDARD, PASSWORD)
    # yield
    # InventoryPage(browser).delete_all_in_shopping_cart_container()
