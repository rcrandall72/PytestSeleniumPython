from common_strings import *


class Driver:
    def __init__(self, driver=None):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def set_driver(self, new_driver):
        self.driver = new_driver


class TestSettings:
    def __init__(self, user_type=UserData.STANDARD_USER, browser=Browsers.CHROME, url=URLs.SAUCE_DEMO):
        self.user_type = user_type
        self.browser = browser
        self.url = url

    def set_test_settings(self, user_type, browser, url):
        self.user_type = user_type
        self.browser = browser
        self.url = url

