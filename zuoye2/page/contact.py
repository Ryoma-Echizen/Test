from selenium.webdriver.common.by import By

from zuoye2.page.base_page import BasePage


class Contact(BasePage):
    def add_member(self,data):
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')  # ".ww_radio+span:contains('女')"
        mobile_locator = (By.NAME, 'mobile')
        self.find(name_locator).send_keys('oyxf')
        self.find(acctid_locator).send_keys('oyxf')
        self.find(gender_locator).click()
        self.find(mobile_locator).send_keys('12000000001')
