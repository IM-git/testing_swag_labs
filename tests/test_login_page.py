import allure

import time

import pytest

from pages import LoginPage

from src import Login

from credential import Credential

LOGINS_PASSWORD_LIST = [(login, Credential.PASSWORD) for login in Credential.LOGIN_LIST]


class TestLoginPage:
    """
    Notices:
    When switch to the English language,
    some words aren't translated into English.
    """

    @allure.feature("Login page.")
    @allure.link(url=Login.LINK, name='LOGIN_LINK')
    @pytest.mark.parametrize('login, password', LOGINS_PASSWORD_LIST)
    def test_login(self, browser, login, password):
        """
        Checking login form.
        """

        login_page = LoginPage(browser, Login.LINK)
        login_page.open_page()
        login_page.check_url()
        login_page.enter_login(login)
        login_page.enter_password(password)
        login_page.click_login_button()
        time.sleep(1)

    @allure.feature("Login page.")
    @allure.link(url=Login.LINK, name='LOGIN_LINK')
    def test_login_locked_out(self, browser):

        login_page = LoginPage(browser, Login.LINK)
        login_page.open_page()
        login_page.check_url()
        login_page.enter_login(Credential.LOGIN_LOCKED)
        login_page.enter_password(Credential.PASSWORD)
        login_page.click_login_button()
        login_page.check_error_message_locked_user()
        time.sleep(1)
