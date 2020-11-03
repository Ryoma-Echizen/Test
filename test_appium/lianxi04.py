# 雪球app切换到交易，选择港美股开户，输入手机、错误的验证码点击立即开户，返回
# MuMU模拟器6.0测试通过
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLianxi04:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['devicesName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset'] = True
        caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def test_lianxi04_native(self):
        #方法1-模拟器mumu测试通过
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, '港美股开户').click()
        # 滑动
        self.test_scroll()
        phone = (By.XPATH, '//android.webkit.WebView[@content-desc="雪盈证券"]/android.view.View[2]')
        self.driver.find_element(*phone).click()
        phone_list = [8, 12, 10, 8, 13, 7, 10, 13, 14, 16, 15]
        # 输入手机号15316036798
        for i in phone_list:
            self.driver.press_keycode(i)
        code = (By.XPATH, '//android.webkit.WebView[@content-desc="雪盈证券"]/android.view.View[3]')
        self.driver.find_element(*code).click()
        code_list = [8, 9, 10, 115]
        # 输入验证码1234
        for i in code_list:
            self.driver.press_keycode(i)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, '立即开户').click()
        self.driver.find_element(By.ID, 'action_bar_close').click()

    def test_lianxi04_context(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, '港美股开户').click()

        # self.driver.find_element(By.CSS_SELECTOR,'.trade_home_xueying_SJY').click()
        WebDriverWait(self.driver,30).until(lambda x : len(self.driver.window_handles) > 3)
        self.test_scroll()
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'[placeholder="请输入手机号"]')))
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入手机号"]').send_keys('15316036798')
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入验证码"]').send_keys('1234')
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(By.ID,'action_bar_back').click()



    # 滚动TouchAction
    def test_scroll(self):
        size = self.driver.get_window_size()
        for i in range(3):
            TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
                .release() \
                .perform()