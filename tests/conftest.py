import pytest

from tools import Browser
from tools import DataSettings

from pages import LoginPage
from pages import InventoryPage

from src import Login

from settings import LOGIN_STANDARD, PASSWORD


@pytest.fixture(scope='session')
def browser():
    """
    Initialization browser driver.
    """
    data = DataSettings.config_data()
    driver = Browser.browser_(data)
    driver.implicitly_wait(data["wait_time"])
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def authorization(browser):
    """Using for authorization on the site(standard option)."""
    LoginPage(browser, Login.LINK).authorization(LOGIN_STANDARD, PASSWORD)
