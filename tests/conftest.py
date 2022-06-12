import pytest

from tools import Browser
from tools import DataSettings


@pytest.fixture(scope='session')
def browser():
    """
    Initialization browser driver.
    """
    data = DataSettings.config_data()
    driver = Browser.browser_(data)
    driver.implicitly_wait(data["wait_time"])
    driver.maximize_window()
    yield driver
    driver.quit()
