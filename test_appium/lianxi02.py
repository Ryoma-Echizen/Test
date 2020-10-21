#搜索股票，点击股票分类，选择香港上市的阿里巴巴股票，并断言大于200

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.common.by import By



class TestLianxi01:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        # caps['deviceName'] = 'Test_9.0'
        caps['deviceName'] = '2KE0219B09101306'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset'] = True
        caps['dontStopAppOnReset'] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)


    #获取香港阿里巴巴的股票价格并断言大于200，添加自选，点击下次再说
    def test_search_and_get_price_hk(self):
        # self.driver.find_element(MobileBy.ID, 'tv_agree').click()
        self.driver.find_element(MobileBy.ID, 'home_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.ID, 'name').click()
        #切到股票title
        stock= (By.XPATH,"//*[contains(@resource-id,'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        #获取阿里巴巴香港股票价格
        current_price =(By.XPATH,"//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]")
        print(float(self.driver.find_element(*current_price).text))
        assert float(self.driver.find_element(*current_price).text) > 200
        print(self.driver.find_element(*current_price).get_attribute("resourceId"))







