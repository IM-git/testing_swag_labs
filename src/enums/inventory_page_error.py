from enum import Enum


class InventoryPageError(Enum):

    ERROR = "(>_<)## ERROR!!"
    SIDEBAR_NOT_DISPLAYED = "Menu sidebar isn't displaying!!"
    SIDEBAR_IS_DISPLAYED = "Menu sidebar is displaying!!"
    WRONG_AFTER_RESET_SHOPPING_CART_BADGE = "Shopping cart badge have to be empty."
    WRONG_WEBPAGE = "This isn't an expected webpage!!"
    WRONG_VALUE_OF_THE_STATE = "An incorrect status value was received!!"
    WRONG_QUANTITY_SHOPPING_CART_BADGE =\
        "The number of selected items" \
        "doesn't match the value in the shopping cart badge!!"
    WRONG_DESCENDING_SORT_ORDER = "Sequence of the values by descending sort order is wrong!!"
