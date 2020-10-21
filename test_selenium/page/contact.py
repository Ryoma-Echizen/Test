from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    # __add_member_button = (By.CSS,'XXXX')
    def add_member(self,data):
        name_locator = (By.NAME,'username')
        acctid_locator = (By.NAME,'acctid')
        gender_locator = (By.CSS_SELECTOR,'.ww_radio[value="2"]')#".ww_radio+span:contains('女')"
        mobile_locator = (By.NAME, 'mobile')
        self.find(name_locator).send_keys('oyxf')
        self.find(acctid_locator).send_keys('oyxf')
        self.find(gender_locator).click()
        self.find(mobile_locator).send_keys('12000000001')




        return self

    def add_member_error(self,data):
        return AddMemberPage()

    def search(self,name):
        pass

    def import_users(self,data):
        pass

    def export_users(self):
        pass

    def set_department(self,data):
        pass

    def delete(self):
        pass

    def add_department(self):
        pass
