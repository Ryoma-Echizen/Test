from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWXmicro:
    def setup(self):
        # caps["chromedriverExecutableDir"] = "/Users/"
        # caps["chromedriverExecutable"] = "/Users/"
        # caps["chromedriverExecutable"] = "/usr/bin/chromedriver"

        caps = {}
        caps["platformName"] = "android"
        # caps["deviceName"] = "192.168.56.104:5555"
        caps["deviceName"] = "192.168.2.7:1212"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        # caps['unicodeKeyboard'] = True
        # caps['resetKeyboard'] = True

        # caps['chromedriverExecutable'] = '/usr/bin/chromedriver'

        # options = ChromeOptions()
        # options.add_experimental_option('androidProcess', 'com.tencent.mm:appbrand0')
        caps['chromeOptions'] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }

        caps['adbPort'] = 5038

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        # self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)
        self.enter_micro_program()

    def enter_micro_program(self):
        # 原生自动化测试
        #向下滑动
        self.driver.implicitly_wait(2)
        self.swipe_down(500,1)
        sleep(3)
        #点击雪球小程序
        self.driver.find_element(By.ID,'com.tencent.mm:id/cna').click()
        sleep(3)
        print(self.driver.contexts)  # NATIVE_APP

    # 向下滑动
    def swipe_down(self, t, n):
        size = self.driver.get_window_size()
        print(size)
        x1 = size['width'] * 0.5  # x坐标
        y1 = size['height'] * 0.25  # 起点y坐标
        y2 = size['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def test_search_webview(self):
        sleep(10)
        for i in self.driver.contexts:
            print(i)
        # 进入webview 名称错误
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        print(self.driver.contexts[-1])
        self.driver.switch_to.context(self.driver.contexts[-1])
        # self.driver.switch_to.context('WEBVIEW_com.tencent.mm.xxx')
        self.driver.implicitly_wait(10)

        # # tap触摸
        self.driver.tap([(438, 1131), (738, 1434)], 1000)

        # css定位
        # self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # self.driver.find_element(By.CLASS_NAME, 'android.widget.Image').click()
        # # 等待新窗口
        # WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        # self.find_top_window()
        # self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # # 输入
        # self.driver.switch_to.context("NATIVE_APP")
        # ActionChains(self.driver).send_keys("alibaba").perform()
        # # 点击
        # self.driver.switch_to.context('WEBVIEW_xweb')
        # self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        # self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()
