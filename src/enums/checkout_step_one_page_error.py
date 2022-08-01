from enum import Enum


class CheckoutStepOnePageError(Enum):

    WRONG_FILLED_FORM = "Was incorrectly filled out form!!"
    WRONG_WEBPAGE = "This isn't an expected webpage!!"
