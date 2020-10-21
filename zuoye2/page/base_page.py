from selenium import webdriver

class BasePage:
    _base_url=""
    def __init__(self,reuse=False):
        if reuse:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
        else:
            self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(3)

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):
        if isinstance(by,tuple):
            return self._driver.find_element(*by)
        else:
            return  self._driver.find_element(by,locator)

