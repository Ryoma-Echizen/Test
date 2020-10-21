from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestApiDemo:
    def setup(self):
        caps = {}
        caps['platformName'] ='android'
        caps['devicesName'] ='2KE0219B09101306'
        caps['appPackage']= 'io.appium.android.apis'
        caps['appActivity']='.ApiDemos'
        caps['noReset']= True
        caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_toast(self):
        self.driver.find_element(By.XPATH,'//*[contains(@text,"Views")]').click()
        # 滚动到Popup Menu
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click()
        self.driver.find_element(By.XPATH,'//*[contains(@text,"Search")]').click()
        toast = self.driver.find_element(By.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "Clicked popup menu item Search" in toast

