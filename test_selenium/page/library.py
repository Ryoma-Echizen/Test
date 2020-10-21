from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Library(BasePage):
    def add_pic(self,path):
        self.find((By.CSS_SELECTOR,'.ww_icon_GrayPic')).click()
        self.find((By.CSS_SELECTOR,'.js_upload_file_selector')).click()
        self.find((By.CSS_SELECTOR,'.material_upload_input')).send_keys(path)
        self.find(By.CSS_SELECTOR,'.ww_dialog_foot.ww_diaglog_foot_cnt > a').click()

