from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class Search(BasePage):
    _name_locator = (MobileBy.ID,'name')
    def search(self,key:str):
        self._driver.find_element(MobileBy.ID, 'search_input_text').send_keys(key)
        self.find(self._name_locator).click()
        return self

    def get_price(self,stock_type : str) ->float:
        # self._driver.find_element(MobileBy.ID, stock_type).click()
        return float(self._driver.find_element(MobileBy.ID, 'current_price').text)

    def add_select(self):
        self.find_by_text("加自选").click()