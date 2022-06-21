import allure

import time

import pytest

from pages import LoginPage

from src import Login

from settings import *

LOGINS_PASSWORD_LIST = [(login, PASSWORD) for login in LOGIN_LIST]


@allure.feature("Login page.")
@allure.link(url=Login.LINK, name='LOGIN_PAGE_LINK')
class TestLoginPage:
    """
    Testing of the login page.
    """

    @pytest.mark.parametrize('login', LOGIN_LIST)
    def test_logins(self, browser, login):
        """
        Checking login form.
        Added in parametrize only login's value,
        because in allure report shows data.
        """

        login_page = LoginPage(browser, Login.LINK)
        login_page.open_page()
        login_page.check_url()
        login_page.check_status_code()
        login_page.enter_login(login)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        time.sleep(1)

    def test_login_locked_out(self, browser):
        """
        Checking a text which appear
        after failed login attempt.
        """

        login_page = LoginPage(browser, Login.LINK)
        login_page.open_page()
        login_page.check_url()
        login_page.check_status_code()
        login_page.enter_login(LOGIN_LOCKED)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        login_page.check_error_message_locked_user()
        time.sleep(1)
