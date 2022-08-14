from selenium.webdriver.common.by import By

from .base import Base


class CheckoutStepTwo(Base):

    LINK = 'https://www.saucedemo.com/checkout-step-two.html'
    LINK_CHECKOUT_INVENTORY = 'https://www.saucedemo.com/inventory.html'
    LINK_CHECKOUT_STEP_ONE = 'https://www.saucedemo.com/checkout-step-one.html'
    LINK_CHECKOUT_COMPLETE = 'https://www.saucedemo.com/checkout-complete.html'

    CANCEL_BUTTON = (By.CSS_SELECTOR, '#cancel')
    FINISH_BUTTON = (By.CSS_SELECTOR, '#finish')

    SUMMARY_INFO = (By.CSS_SELECTOR, '.summary_info')
