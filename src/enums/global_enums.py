from enum import Enum


class GlobalErrorMessages(Enum):
    """Messages for asserts in test files."""

    UNKNOWN_VALUE = "Unknown value!!"

    WRONG_STATUS_CODE = 'Received status code is not equal to expected!!'
    WRONG_TITLE_PAGE = 'Another page is open!!'
    WRONG_IS_DISPLAYED = 'The page is not loaded!!'
    WRONG_PAGE = 'Other page was expected to load!!'
