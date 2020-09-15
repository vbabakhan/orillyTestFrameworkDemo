import traceback
from selenium import webdriver
import os


class WebDriverFactory:

    def __init__(self, browser):

        self.browser = browser

    def get_web_driver_instance(self):

        base_url = "https://www.oreillyauto.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path='geckodriver')
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)
        return driver
