from selenium.webdriver.common.by import By

from .base import Base


class Login(Base):
    LINK = Base.LINK

    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    LOGIN_INPUT = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    IMAGE_BOT = (By.CSS_SELECTOR, '.bot_column')
    TEXT_ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    ERROR_TEXT = 'Epic sadface: Sorry, this user has been locked out.'
