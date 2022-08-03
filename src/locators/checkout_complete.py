from selenium.webdriver.common.by import By

from .base import Base


class CheckoutComplete(Base):

    LINK = 'https://www.saucedemo.com/checkout-complete.html'
    LINK_INVENTORY = 'https://www.saucedemo.com/inventory.html'

    BACK_HOME_BUTTON = (By.CSS_SELECTOR, '#back-to-products')
    PONY_EXPRESS_IMG = (By.CSS_SELECTOR, '.pony_express')
    COMPLETE_TEXT = (By.CSS_SELECTOR, '.complete-text')
