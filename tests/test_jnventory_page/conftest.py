import pytest
from pages import LoginPage
from src import Login
from credential import Credential


@pytest.fixture(scope="function", autouse=True)
def authorization(browser):
    LoginPage(browser, Login.LINK).authorization(Credential.LOGIN_STANDARD, Credential.PASSWORD)
