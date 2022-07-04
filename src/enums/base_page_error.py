from enum import Enum


class BasePageError(Enum):
    """Messages for asserts in test files."""

    UNKNOWN_VALUE = "Unknown value!!"
    SIDEBAR_IS_DISPLAYED = "Menu sidebar is displaying!!"
    SIDEBAR_NOT_DISPLAYED = "Menu sidebar isn't displaying!!"

    WRONG_AFTER_RESET_SHOPPING_CART_BADGE = "Shopping cart badge have to be empty."
    WRONG_STATUS_CODE = 'Received status code is not equal to expected!!'
    WRONG_TITLE_PAGE = 'Another page is open!!'
    WRONG_IS_DISPLAYED = 'The page is not loaded!!'
    WRONG_PAGE = 'Other page was expected to load!!'
    WRONG_WEBPAGE = "This isn't an expected webpage!!"
