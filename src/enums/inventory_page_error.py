from enum import Enum


class InventoryPageError(Enum):

    ERROR = "(>_<)## ERROR!!"
    SIDEBAR_NOT_DISPLAYED = "Menu sidebar isn't displaying!!"
    SIDEBAR_IS_DISPLAYED = "Menu sidebar is displaying!!"
    WRONG_WEBPAGE = "This isn't an expected webpage!!"
    WRONG_QUANTITY_SHOPPING_CART_BADGE =\
        "The number of selected items" \
        "doesn't match the value in the shopping cart badge!!"
