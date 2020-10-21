from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.library import Library


class Management(BasePage):
    _base_url ='https://work.weixin.qq.com/wework_admin/frame#manageTools'
    def library(self):
        self.find((By.CSS_SELECTOR,'.manageTools_cnt_items > li:nth-child(5)')).click()
        return Library(reuse=True)
