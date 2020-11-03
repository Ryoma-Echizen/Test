from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package ='com.xueqiu.android'
    _activity ='.view.WelcomeActivityAlias'
    def start(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = '127.0.0.1:7555'
        # caps['platformVersion'] = '6.0.1'
        caps['appPackage'] = self._package
        caps['appActivity'] = self._activity
        caps['noReset'] = True
        # caps['dontStopAppOnReset'] = True
        # caps['unicodeKeyboard'] = True
        # caps['resetKeyboard'] = True
        caps['skipServerInstallation'] = True
        # caps["chromedriverExecutableDir"] = "/Users/"
        # caps["chromedriverExecutable"] = "/Users/"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) ->Main:
        def wait_load():
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return  True
            if "image_cancel" in source:
                return  True
            return False
        WebDriverWait(self.driver,30).until(wait_load)
        return Main(self._driver)
