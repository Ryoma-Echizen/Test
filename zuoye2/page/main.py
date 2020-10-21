from selenium.webdriver.common.by import By

from zuoye2.page.base_page import BasePage
from zuoye2.page.contact import Contact


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def add_member(self):
        self.find(By.CSS_SELECTOR,'[node-type="addmember"]').click()
        return Contact(reuse=True)