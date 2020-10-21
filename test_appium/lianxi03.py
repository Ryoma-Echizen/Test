#添加某只股票到自选，然后再次搜索并验证(不要使用文字内容判断，使用get attribute
#测试通过 华为真机
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestLianxi03:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'Test_9.0'
        # caps['deviceName'] = '2KE0219B09101306'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset'] = False
        caps['dontStopAppOnReset'] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_add_stock(self):
        self.driver.find_element(MobileBy.ID, 'tv_agree').click()
        self.driver.find_element(MobileBy.ID, 'home_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('兔宝')
        self.driver.find_element(By.XPATH, '//*[@text="SZ002043"]').click()
        sleep(3)
        # stock = (By.XPATH,'//*[contains(@resource-id,"title_container")]//*[@text="股票"]')
        # self.driver.find_element(*stock).click()
        self.driver.find_element(By.XPATH,'//*[contains(@resource-id,"title_container")]//*[@text="股票"]').click()
        #点击添加
        # btn = self.driver.find_element(MobileBy.ID,'follow_btn')
        # print(btn.get_attribute("resourceId"))
        add_btn = (By.XPATH, "//*[@text='兔宝宝']/../../..//*[contains(@resource-id,'follow_btn')]")
        self.driver.find_element(*add_btn).click()
        #点击下次再说
        self.driver.find_element(MobileBy.ID,'tv_left').click()
        #点击取消
        self.driver.find_element(MobileBy.ID,'action_close').click()
        # 重复搜索
        self.driver.find_element(MobileBy.ID, 'home_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('兔宝')
        self.driver.find_element(By.XPATH, '//*[@text="SZ002043"]').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[contains(@resource-id,"title_container")]//*[@text="股票"]').click()
        added_btn = self.driver.find_element(By.XPATH, "//*[@text='兔宝宝']/../../..//*[contains(@resource-id,'followed_btn')]").get_attribute('text')
        assert "已添加" == added_btn





