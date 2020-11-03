from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.search import Search


class Main(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, 'home_search').click()
        return Search()



    def goto_profile(self):
        pass

    def goto_stock(self):
        pass

