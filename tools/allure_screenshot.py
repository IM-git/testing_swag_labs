import allure
from allure_commons.types import AttachmentType


class AllureScreenshot:

    def __init__(self):
        pass

    def make_screenshot(self, driver):
        with allure.step("Make screenshot"):
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)


def taking_screenshot(browser):
    AllureScreenshot().make_screenshot(browser)
