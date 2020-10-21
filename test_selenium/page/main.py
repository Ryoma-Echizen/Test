from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact
from test_selenium.page.message import Message


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    def download(self):
        pass

    def import_users(self,path):
        self.find((By.PARTIAL_LINK_TEXT,'导入通讯录')).click()
        self.find((By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_uploadInputMask')).send_keys(path)
        self.find((By.CSS_SELECTOR,'.ww_fileImporter_submit')).click()
        self.find((By.CSS_SELECTOR,'.ww_btn_Back')).click()
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def send_message(self):
        self.find((By.LINK_TEXT, '消息群发')).click()
        return Message(reuse=True)

    def get_message(self):
        return ['aaa','bbb']

    def add_member(self):
        self.find(By.CSS_SELECTOR,'[node-type="addmember"]').click()
        # location = (By.LINK_TEXT,'添加成员')
        # self._driver.execute_script('arguments[0].click();',self.find(location))
        return Contact(reuse=True)

