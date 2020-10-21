#使用已经存在的chrome进程进如企业微信添加通讯录，，目前元素等待报错，
import time
from  selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_003():
    def setup(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chromeOptions)

    def test_add(self):
        WebDriverWait(self.driver,10).until(self.wait_element)
        self.driver.find_element(By.CSS_SELECTOR,'.js_has_member div:nth-child(1) .js_add_member').click()
        time.sleep(1)
        self.driver.find_element(By.ID,'username').send_keys('test1')
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('test1')
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys('11111111112')
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()

    def teardown(self):
        self.driver.quit()

    def wait_element(self,x):
        size = len(self.driver.find_element(By.ID,'username'))
        if size < 1:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member')))
        return  size >= 1




