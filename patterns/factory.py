import os

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SChrome
from selenium.webdriver.chrome.options import Options as OChrome
from selenium.webdriver.firefox.service import Service as SFirefox
from selenium.webdriver.firefox.options import Options as OFirefox

from tools.exceptions.unknown_browser import UnknownBrowser

from credential import Credential

from selenoid import capabilities


class Factory:
    """Pattern for creating specific
    version browser: Google Chrome, FireFox."""

    @staticmethod
    def get_browser(config):
        """Selecting the browser option based on the parameters"""
        if config['browser'] == 'chrome':
            return Factory.chrome_browser()
        elif config['browser'] == 'firefox':
            return Factory.firefox_browser()
        elif config['browser'] == 'chrome_selenoid':
            return Factory.chrome_browser_selenoid()
        elif config['browser'] == 'firefox_selenoid':
            return Factory.firefox_browser_selenoid()
        else:
            raise UnknownBrowser(Factory.config_browser(config))
            # raise Exception(f' We are not use the "{Factory.config_browser(config)}".')

    @staticmethod
    def chrome_browser():
        """Browser option for using Google Chrome."""
        option = OChrome()
        # to supress the error messages/logs
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_service = SChrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=option)
        return driver

    @staticmethod
    def firefox_browser():
        """Browser option for using FireFox."""
        os.environ['GH_TOKEN'] = Credential.TOKEN
        option = OFirefox()
        firefox_service = SFirefox(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service, options=option)
        return driver

    @staticmethod
    def chrome_browser_selenoid():
        """Browser option for using Google Chrome
        from selenoid container."""
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions()
        )
        return driver

    @staticmethod
    def firefox_browser_selenoid():
        """Browser option for using FireFox
        from selenoid container."""
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.FirefoxOptions()
        )
        return driver

    @staticmethod
    def any_browser_selenoid():
        """Instead of to use several methods,
         can use one unique method for all browsers.
         Will need to change the values in 'capabilities'. """
        driver = webdriver.Remote(
            command_executor="127.0.0.1:4444/wd/hub",
            desired_capabilities=capabilities)
        return driver

    @staticmethod
    def config_browser(config):
        """Checking correct value browser in the config file
        for creating browser session."""
        if 'browser' not in config:
            print('The config file does not contain "browser"')
        elif config['browser'] not in ['chrome', 'firefox']:
            print(f' We are not use the "{config["browser"]}".')
        return config['browser']
