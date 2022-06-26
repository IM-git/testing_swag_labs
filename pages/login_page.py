from pages import BasePage

from elements import Elements
from elements import MouseActions
from elements import KeyboardActions
from elements.base_element import BaseElement

from src import Login
from src import StatusCodes
from src import LoginPageError
from src import LoginPageText

from tools import Logger
from tools import DataSettings

DATA = DataSettings.config_data()


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.elements = Elements(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)
        self.mouse_actions = MouseActions(self.browser)

    def authorization(self, login, password):
        self.open_page()
        self.check_url()
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()

    def click_login_button(self) -> None:
        self.mouse_actions.one_click(Login.LOGIN_BUTTON)

    def enter_login(self, login: str) -> None:
        self.enter_value(login, Login.LOGIN_INPUT)

    def enter_password(self, password: str) -> None:
        self.enter_value(password, Login.PASSWORD_INPUT)

    def check_error_message_locked_user(self):
        self.elements.check_is_displayed(*Login.TEXT_ERROR_MESSAGE)
        got_text = self.elements.get_text(*Login.TEXT_ERROR_MESSAGE)
        assert got_text == LoginPageText.ERROR_TEXT.value,\
            LoginPageError.WRONG_ERROR_MESSAGE.value
