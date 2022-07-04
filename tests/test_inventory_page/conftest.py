import pytest
from pages import LoginPage
from src import Login
from settings import LOGIN_STANDARD, PASSWORD


@pytest.fixture(scope="function", autouse=True)
def authorization(browser):
    LoginPage(browser, Login.LINK).authorization(LOGIN_STANDARD, PASSWORD)
