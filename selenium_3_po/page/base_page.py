from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __int__(self,driver:WebDriver=None):
        if driver == None:
            self._chromeOptions = Options()
            self._chromeOptions.add_experimental_option('debuggerAddress','127.0.0.1')
            self._driver = webdriver.Chrome(options=self._chromeOptions)
        else:
            self._driver = driver
        self.driver.implicitly_wait(2)

    def find_elemnt(self):
        self._driver.find_element_by_id('xxx')