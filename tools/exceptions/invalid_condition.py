from tools.exceptions.base_exception import BaseExceptions


class InvalidConfigCondition(BaseExceptions):
    """
    We use this class for indicate invalid condition exception.
    This type answer is not used in the condition.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Expected of the value in config.json:" \
               f"'yes' or 'not', written: '{self.value}'."


class InvalidConditionInTest(BaseExceptions):
    """
    We use this class for indicate invalid condition exception
    in the tests. This type answer is not used in the condition.
    Appears when 'browser' value in tests entered not correctly
    or missing in the test/s.
    """

    def __init__(self):
        pass

    def __str__(self):
        return f"Check the correct using browser in the test.\n" \
               f"Hint. When using singleton," \
               f"in the test doesn't need paste browser in the class page.\n" \
               f"And vice versa if don't use singleton.\n" \
               f"Example: if singleton - 'yes' => MainPage(browser, Main.LINK);\n" \
               f"if singleton - 'no' => MainPage(Main.LINK);"
