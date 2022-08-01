from selenium.webdriver.common.by import By

from .base import Base


class CheckoutStepOne(Base):

    LINK = 'https://www.saucedemo.com/checkout-step-one.html'
    LINK_CHECKOUT_STEP_TWO = 'https://www.saucedemo.com/checkout-step-two.html'
    LINK_CART = 'https://www.saucedemo.com/cart.html'

    EMPTY_FIELD = ''

    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    FIRST_NAME_ERROR_MESSAGE = (By.CSS_SELECTOR, '')
    FIRST_NAME_ERROR_TEXT = 'Error: First Name is required'
    LAST_NAME_ERROR_MESSAGE = (By.CSS_SELECTOR, '')
    LAST_NAME_ERROR_TEXT = 'Error: Last Name is required'
    POSTAL_CODE_ERROR_MESSAGE = (By.CSS_SELECTOR, '')
    POSTAL_CODE_ERROR_TEXT = 'Error: Postal Code is required'
    LIST_ERROR_TEXTS = [FIRST_NAME_ERROR_TEXT,
                        LAST_NAME_ERROR_TEXT,
                        POSTAL_CODE_ERROR_TEXT]

    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#continue')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '#cancel')

    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#first-name')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#last-name')
    POSTAL_CODE_FIELD = (By.CSS_SELECTOR, '#postal-code')

    CHECKOUT_INFO = (By.CSS_SELECTOR, '.checkout_info')

