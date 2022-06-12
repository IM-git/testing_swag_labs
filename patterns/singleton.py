"""
Singleton is a creative design pattern
that lets you ensure that a class has only one instance,
while providing a global access point to this instance.
"""


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# class WebDriver:
#     """This is singleton for webdriver.
#     Didn't delete it because it's good and simple
#     example for understanding how to work singleton."""
#     class __WebDriver:
#
#         def __init__(self, data):
#             self.driver = Factory().get_browser(data)
#
#     driver = None
#
#     def __init__(self, data):
#         if not self.driver:
#             WebDriver.driver = WebDriver.__WebDriver(data).driver

