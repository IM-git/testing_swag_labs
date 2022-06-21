from selenium.webdriver.common.by import By

from .base import Base


class Inventory(Base):

    LINK = 'https://www.saucedemo.com/inventory.html'
    LINK_CLICK_ABOUT = 'https://saucelabs.com/'
    LINK_CLICK_SHOPPING_CART_CONTAINER = 'https://www.saucedemo.com/cart.html'
    LINK_CLICK_LOGOUT = Base.LINK

    ATTRIBUTE_MENU_SIDEBAR_ARIA_HIDDEN = 'aria-hidden'
    ARIA_HIDDEN_VALUE_IF_SIDEBAR_OPEN = 'false'
    ARIA_HIDDEN_VALUE_IF_SIDEBAR_HIDDEN = 'true'
    REMOVE_STATE = 'REMOVE'
    ADD_STATE = 'ADD TO CART'

    ABOUT_LINK = (By.CSS_SELECTOR, '#about_sidebar_link')
    ALL_ITEMS_LINK = (By.CSS_SELECTOR, '#inventory_sidebar_link')
    FACEBOOK_LINK = (By.CSS_SELECTOR, '.social_facebook a')
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, '.inventory_item_name')

    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_item_price')
    INVENTORY_ITEM_PRICE_XPATH = (By.XPATH, '//div[@class="inventory_item_price"]')

    LINKEDIN_LINK = (By.CSS_SELECTOR, '.social_linkedin a')
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_sidebar_link')
    MENU_SIDEBAR = (By.CSS_SELECTOR, '.bm-menu-wrap')
    MENU_SIDEBAR_BUTTON = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    MENU_SIDEBAR_CLOSE = (By.CSS_SELECTOR, '#react-burger-cross-btn')
    PRODUCT_SORT_CONTAINER = (By.CSS_SELECTOR, '.product_sort_container')
    PRODUCT_SORT_BY_AZ = (By.CSS_SELECTOR, '[value="az"]')
    PRODUCT_SORT_BY_ZA = (By.CSS_SELECTOR, '[value="za"]')
    PRODUCT_SORT_BY_LOW_TO_HIGH = (By.CSS_SELECTOR, '[value="lohi"]')
    PRODUCT_SORT_BY_HIGH_TO_LOW = (By.CSS_SELECTOR, '[value="hilo"]')

    PRODUCT_SORT_BY = [PRODUCT_SORT_BY_AZ,
                       PRODUCT_SORT_BY_ZA,
                       PRODUCT_SORT_BY_LOW_TO_HIGH,
                       PRODUCT_SORT_BY_HIGH_TO_LOW]
    INVENTORY_ITEM_PRICES = [(By.XPATH, '(// div[@class ="inventory_item_price"])[1]'),
                             (By.XPATH, '(// div[@class ="inventory_item_price"])[2]'),
                             (By.XPATH, '(// div[@class ="inventory_item_price"])[3]'),
                             (By.XPATH, '(// div[@class ="inventory_item_price"])[4]'),
                             (By.XPATH, '(// div[@class ="inventory_item_price"])[5]'),
                             (By.XPATH, '(// div[@class ="inventory_item_price"])[6]')]
    INVENTORY_ITEM_NAMES = [(By.XPATH, '(// div[@class ="inventory_item_name"])[1]'),
                            (By.XPATH, '(// div[@class ="inventory_item_name"])[2]'),
                            (By.XPATH, '(// div[@class ="inventory_item_name"])[3]'),
                            (By.XPATH, '(// div[@class ="inventory_item_name"])[4]'),
                            (By.XPATH, '(// div[@class ="inventory_item_name"])[5]'),
                            (By.XPATH, '(// div[@class ="inventory_item_name"])[6]')]

    RESET_APP_STATE_LINK = (By.CSS_SELECTOR, '#reset_sidebar_link')
    TWITTER_LINK = (By.CSS_SELECTOR, '.social_twitter a')

    ADD_SAUCE_LABS_BACKPACK_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    ADD_SAUCE_LABS_BIKE_LIGHT_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    ADD_SAUCE_LABS_BOLT_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_SAUCE_LABS_FLEECE_JACKET_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket')
    ADD_SAUCE_LABS_ONESIE_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    ADD_SAUCE_LABS_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '[id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    REMOVE_SAUCE_LABS_BACKPACK_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    REMOVE_SAUCE_LABS_BIKE_LIGHT_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-bike-light')
    REMOVE_SAUCE_LABS_BOLT_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-bolt-t-shirt')
    REMOVE_SAUCE_LABS_FLEECE_JACKET_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-fleece-jacket')
    REMOVE_SAUCE_LABS_ONESIE_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-onesie')
    REMOVE_SAUCE_LABS_T_SHIRT_BUTTON = (By.CSS_SELECTOR, '[id="remove-test.allthethings()-t-shirt-(red)"]')

    SAUCE_LABS_BACKPACK_BUTTON = [ADD_SAUCE_LABS_BACKPACK_BUTTON, REMOVE_SAUCE_LABS_BACKPACK_BUTTON]
    SAUCE_LABS_BIKE_LIGHT_BUTTON = [ADD_SAUCE_LABS_BIKE_LIGHT_BUTTON, REMOVE_SAUCE_LABS_BIKE_LIGHT_BUTTON]
    SAUCE_LABS_BOLT_T_SHIRT_BUTTON = [ADD_SAUCE_LABS_BOLT_T_SHIRT_BUTTON, REMOVE_SAUCE_LABS_BOLT_T_SHIRT_BUTTON]
    SAUCE_LABS_FLEECE_JACKET_BUTTON = [ADD_SAUCE_LABS_FLEECE_JACKET_BUTTON, REMOVE_SAUCE_LABS_FLEECE_JACKET_BUTTON]
    SAUCE_LABS_ONESIE_BUTTON = [ADD_SAUCE_LABS_ONESIE_BUTTON, REMOVE_SAUCE_LABS_ONESIE_BUTTON]
    SAUCE_LABS_T_SHIRT_BUTTON = [ADD_SAUCE_LABS_T_SHIRT_BUTTON, REMOVE_SAUCE_LABS_T_SHIRT_BUTTON]

    ADD_SAUCE_LABS_PRODUCT_BUTTONS_LIST = [SAUCE_LABS_BACKPACK_BUTTON,
                                           SAUCE_LABS_BIKE_LIGHT_BUTTON,
                                           SAUCE_LABS_BOLT_T_SHIRT_BUTTON,
                                           SAUCE_LABS_FLEECE_JACKET_BUTTON,
                                           SAUCE_LABS_ONESIE_BUTTON,
                                           SAUCE_LABS_T_SHIRT_BUTTON]
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')

    SHOPPING_CART_CONTAINER = (By.CSS_SELECTOR, '#shopping_cart_container')
