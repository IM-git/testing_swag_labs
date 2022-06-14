from selenium.webdriver.common.by import By

from .base import Base


class Inventory(Base):

    LINK = 'https://www.saucedemo.com/inventory.html'

    ABOUT_LINK = (By.CSS_SELECTOR, '#about_sidebar_link')
    ALL_ITEMS_LINK = (By.CSS_SELECTOR, '#inventory_sidebar_link')
    FACEBOOK_LINK = (By.CSS_SELECTOR, '.social_facebook a')
    LINKEDIN_LINK = (By.CSS_SELECTOR, '.social_linkedin a')
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_sidebar_link')
    MENU_BUTTON = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    MENU_SIDEBAR = (By.CSS_SELECTOR, '.bm-menu-wrap')
    MENU_SIDEBAR_CLOSE = (By.CSS_SELECTOR, '#react-burger-cross-btn')
    PRODUCT_SORT_CONTAINER = (By.CSS_SELECTOR, '.product_sort_container')
    PRODUCT_SORT_BY_AZ = (By.CSS_SELECTOR, '[value="az"]')
    PRODUCT_SORT_BY_ZA = (By.CSS_SELECTOR, '[value="za"]')
    PRODUCT_SORT_BY_LOW_TO_HIGH = (By.CSS_SELECTOR, '[value="lohi"]')
    PRODUCT_SORT_BY_HIGH_TO_LOW = (By.CSS_SELECTOR, '[value="hilo"]')
    RESET_APP_STATE_LINK = (By.CSS_SELECTOR, '#reset_sidebar_link')
    TWITTER_LINK = (By.CSS_SELECTOR, '.social_twitter a')
    SAUCE_LABS_BACKPACK_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    SAUCE_LABS_BIKE_LIGHT_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    SAUCE_LABS_BOLT_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    SAUCE_LABS_FLEECE_JACKET_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket')
    SAUCE_LABS_ONESIE_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    SAUCE_LABS_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '[id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    SAUCE_LABS_PRODUCT_BUTTONS_LIST = [SAUCE_LABS_BACKPACK_BUTTON,
                                       SAUCE_LABS_BIKE_LIGHT_BUTTON,
                                       SAUCE_LABS_BOLT_T_SHIRT_BUTTON,
                                       SAUCE_LABS_FLEECE_JACKET_BUTTON,
                                       SAUCE_LABS_ONESIE_BUTTON,
                                       SAUCE_LABS_T_SHIRT_BUTTON]
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')

    SHOPPING_CART_CONTAINER = (By.CSS_SELECTOR, '#shopping_cart_container')
