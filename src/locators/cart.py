from selenium.webdriver.common.by import By

from .base import Base


class Cart(Base):

    LINK = 'https://www.saucedemo.com/cart.html'
    LINK_INVENTORY_PAGE = 'https://www.saucedemo.com/inventory.html'
    LINK_CHECKOUT_STEP_ONE = 'https://www.saucedemo.com/checkout-step-one.html'
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, '#continue-shopping')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')
    PRODUCTS = 'products'
    CHECKOUT_STEP_ONE_TITLE = 'checkout: your information'

    REMOVE_SAUCE_LABS_BACKPACK_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    REMOVE_SAUCE_LABS_BIKE_LIGHT_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-bike-light')
    REMOVE_SAUCE_LABS_BOLT_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-bolt-t-shirt')
    REMOVE_SAUCE_LABS_FLEECE_JACKET_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-fleece-jacket')
    REMOVE_SAUCE_LABS_ONESIE_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-onesie')
    REMOVE_SAUCE_LABS_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '[id="remove-test.allthethings()-t-shirt-(red)"]')

    SAUCE_LABS_BACKPACK_LINK = (By.CSS_SELECTOR, '#item_4_title_link')
    SAUCE_LABS_BIKE_LIGHT_LINK = (By.CSS_SELECTOR, '#item_0_title_link')
    SAUCE_LABS_BOLT_T_SHIRT_LINK = (By.CSS_SELECTOR, '#item_1_title_link')
    SAUCE_LABS_FLEECE_JACKET_LINK = (By.CSS_SELECTOR, '#item_5_title_link')
    SAUCE_LABS_ONESIE_LINK = (By.CSS_SELECTOR, '#item_2_title_link')
    SAUCE_LABS_T_SHIRT_LINK = (By.CSS_SELECTOR, '#item_3_title_link')

    CART_QUANTITY = (By.XPATH, '(// div[@class="cart_quantity"])')  # Need to add [num] necessary number
    CART_QUANTITIES = [(By.XPATH, '(// div[@class="cart_quantity"])[1]'),
                       (By.XPATH, '(// div[@class="cart_quantity"])[2]'),
                       (By.XPATH, '(// div[@class="cart_quantity"])[3]'),
                       (By.XPATH, '(// div[@class="cart_quantity"])[4]'),
                       (By.XPATH, '(// div[@class="cart_quantity"])[5]'),
                       (By.XPATH, '(// div[@class="cart_quantity"])[6]')]

    INVENTORY_ITEM_PRICE = (By.XPATH, '(// div[@class="inventory_item_price"])')    # Need to add [num] necessary number
    INVENTORY_ITEM_PRICES = [(By.XPATH, '(// div[@class="inventory_item_price"])[1]'),
                             (By.XPATH, '(// div[@class="inventory_item_price"])[2]'),
                             (By.XPATH, '(// div[@class="inventory_item_price"])[3]'),
                             (By.XPATH, '(// div[@class="inventory_item_price"])[4]'),
                             (By.XPATH, '(// div[@class="inventory_item_price"])[5]'),
                             (By.XPATH, '(// div[@class="inventory_item_price"])[6]')]

    PRODUCT_SORT_CONTAINER = (By.CSS_SELECTOR, '.product_sort_container')
