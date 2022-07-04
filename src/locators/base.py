from selenium.webdriver.common.by import By

import pytest


class Base:
    TIME = 10
    LINK = "https://www.saucedemo.com/"
    LINK_CLICK_ABOUT = 'https://saucelabs.com/'

    ATTRIBUTE_MENU_SIDEBAR_ARIA_HIDDEN = 'aria-hidden'
    ARIA_HIDDEN_VALUE_IF_SIDEBAR_OPEN = 'false'
    ARIA_HIDDEN_VALUE_IF_SIDEBAR_HIDDEN = 'true'
    REMOVE_STATE = 'REMOVE'
    ADD_STATE = 'ADD TO CART'

    URL_FACEBOOK = 'https://web.facebook.com/saucelabs?_rdc=1&_rdr'
    URL_LINKEDIN = 'https://www.linkedin.com/company/sauce-labs/?original_referer='
    URL_TWITTER = 'https://twitter.com/saucelabs'

    ALL_ITEMS_LINK = (By.CSS_SELECTOR, '#inventory_sidebar_link')
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_sidebar_link')
    ABOUT_LINK = (By.CSS_SELECTOR, '#about_sidebar_link')
    RESET_APP_STATE_LINK = (By.CSS_SELECTOR, '#reset_sidebar_link')

    MENU_SIDEBAR = (By.CSS_SELECTOR, '.bm-menu-wrap')
    MENU_SIDEBAR_BUTTON = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    MENU_SIDEBAR_CLOSE = (By.CSS_SELECTOR, '#react-burger-cross-btn')

    FACEBOOK_LINK = (By.CSS_SELECTOR, '.social_facebook a')
    LINKEDIN_LINK = (By.CSS_SELECTOR, '.social_linkedin a')
    TWITTER_LINK = (By.CSS_SELECTOR, '.social_twitter a')
    PARAMETRIZE_SOCIAL = [(FACEBOOK_LINK, URL_FACEBOOK),
                          pytest.param(LINKEDIN_LINK, URL_LINKEDIN, marks=pytest.mark.xfail),
                          (TWITTER_LINK, URL_TWITTER)]

    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
    SHOPPING_CART_CONTAINER = (By.CSS_SELECTOR, '#shopping_cart_container')
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, '.shopping_cart_link')
