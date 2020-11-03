#雪球切换到交易，选择港美股开户，输入用手机、错误的验证码点击理解开户，切换为本地，返回
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.mobile import Mobile


class TestLianxi04:
    def setup(self):
        caps={}
        caps['platformName']='android'
        caps['devicesName']='192.168.56.105:5555'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset']=True
        caps['skipServerInstallation']=True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(30)

    def test_lianxi04(self):
        self.driver.find_element(By.XPATH,'//*[text="交易" and contains(@resource-id,"tab")]').click()
        self.driver.find_element(By.XPATH,'//*[text="港美" and contains(@resource-id,"title")]').click()
        # TouchAction(self.driver).tap(x=986, y=2292).perform()
        # TouchAction(self.driver).tap(x=335, y=165).perform()
        self.driver.find_element(By.XPATH,'//*[text="登录/注册"]').click()
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'tv_login_by_phone_or_others').click()
        phone = (MobileBy.ACCESSIBILITY_ID, 'register_phone_number')
        # self.driver.find_element(*phone).click()
        self.driver.find_element(*phone).send_keys('15316036798')
        code = (MobileBy.ACCESSIBILITY_ID, 'register_code')
        # self.driver.find_element(*code).click()
        self.driver.find_element(*code).send_keys('15316036798')
        print(self.driver.contexts)

