from tools import ReadFile
from patterns import Factory
from patterns import Singleton

CONFIG_PATH = "tests/config.json"


class DataSettings(metaclass=Singleton):
    """This class with method create
    one file object for reading."""
    @staticmethod
    def config_data():
        return ReadFile.read_file(CONFIG_PATH)


class WebDriver(metaclass=Singleton):
    """This class create only one webdriver object
    for tests."""
    def __init__(self, data):
        self.driver = Factory().get_browser(data)
