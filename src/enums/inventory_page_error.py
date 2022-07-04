from enum import Enum


#   Think about necessary add BasePageError like a parent class(Inheritance)
class InventoryPageError(Enum):

    ERROR = "(>_<)## ERROR!!"
    WRONG_WEBPAGE = "This isn't an expected webpage!!"  # Exist in the BasePageError
    WRONG_VALUE_OF_THE_STATE = "An incorrect status value was received!!"
    WRONG_QUANTITY_SHOPPING_CART_BADGE =\
        "The number of selected items" \
        "doesn't match the value in the shopping cart badge!!"
    WRONG_DESCENDING_SORT_ORDER = "Sequence of the values by descending sort order is wrong!!"
