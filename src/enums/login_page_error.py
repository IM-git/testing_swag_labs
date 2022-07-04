from enum import Enum


class LoginPageError(Enum):
    
    ERROR_TEXT = 'Epic sadface: Sorry, this user has been locked out.'

    MESSAGE_ERROR_MISSING = "The error message is missing!!"
    MESSAGE_ERROR_NOT_DISPLAYING = "The error message isn't displaying!!"
    WRONG_ERROR_MESSAGE = "Error message doesn't match the expected one!!"
