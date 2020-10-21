import json
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = '192.168.2.7:1212'
        # caps['deviceName'] = '2KE0219B09101306'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset'] = True
        caps['dontStopAppOnReset'] = True
        # caps['unicodeKeyboard'] = True
        # caps['resetKeyboard'] = True
        caps['skipServerInstallation'] = True
        # caps["chromedriverExecutableDir"] = "/Users/"
        # caps["chromedriverExecutable"] = "/Users/"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    #查询
    def test_search(self):
        # el1 = self.driver.find_element_by_id('com.xueqiu.android:id/tv_agree')
        # el1.click()
        # el2 = self.driver.find_element_by_id('com.xueqiu.android:id/home_search')
        # el2.click()
        # el3 = self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text')
        # el3.send_keys('alibaba')
        # self.driver.find_element(MobileBy.ID, 'tv_agree').click()
        self.driver.find_element(MobileBy.ID, 'home_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('alibaba')

    #搜索
    def test_search_and_get_price(self):
        # self.driver.find_element(MobileBy.ID, 'tv_agree').click()
        self.driver.find_element(MobileBy.ID, 'home_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('alibaba')
        time.sleep(3)
        self.driver.find_element(MobileBy.ID, 'name').click()
        assert float(self.driver.find_element(MobileBy.ID,'current_price').text) > 200

    #滚动TouchAction
    def test_scroll(self):
        size = self.driver.get_window_size()
        print(size)
        for i in range(10):
            TouchAction(self.driver).long_press(x = size['width']*0.5,y = size['height']*0.8)\
                .move_to(x = size['width']*0.5,y = size['height']*0.2)\
                .release()\
                .perform()

    def test_devices(self):
        #把应用放在后台5秒再激活
        self.driver.background_app(5)
        #锁屏5秒
        self.driver.lock(5)
        #解锁
        self.driver.unlock()

    #获取香港阿里巴巴的股票价格并断言
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

    def test_source(self):
        print(self.driver.page_source)

    def test_webview_native(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        self.driver.find_element(By.XPATH, '//*[@text,"平安银行"]/..//*[@text="开户"]').click()
        submit = (By.XPATH, '//*[@text,"开户领取"]')
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(submit))
        self.driver.find_element(*submit).click()
        phone = (MobileBy.ID,'phone-number')
        # print(self.driver.page_source.text)
        self.driver.find_element(*phone)
        self.driver.find_element(*phone).send_keys('15316036798')
        # phone = (MobileBy.XPATH, "//android.widget.EditText")
        # self.driver.find_element(*phone)

    def test_webview_context(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()

        # 首次做测试的时候，用于分析当前的上下文
        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(0.5)
        # print(self.driver.page_source)

        # 坑1：webview上下文出现大概有3s的延迟, android 6.0默认支持，其他的需要打开webview调试开关
        # adb shell cat /proc/net/unix | grep  webview
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        # 坑2：chromedriver的版本与chrome版本必须对应
        # 坑3：chromedriver可能会存在无法对应chrome版本的情况，需要使用caps的mapping file或者直接chromedriverExecutable
        # /Users/seveniruby/projects/chromedriver/all/chromedriver_2.20 --url-base=wd/hub --port=8000 --adb-port=5037 --verbose

        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.page_source)
        # print(self.driver.window_handles)

        # 使用chrome inspect分析界面控件，需要代理、需要chrome62及以前的版本都可以
        # Proxying [POST /wd/hub/session/b2fe71d1-3dff-45df-bc2c-52e9195d5b98/element] to [POST http://127.0.0.1:8000/wd/hub/session/790fc7cf4c186545679b24ce5bbd9699/element] with body: {"using":"css selector","value":".trade_home_info_3aI"}
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()

        # 首次做测试的时候，用于分析当前的窗口
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     sleep(0.5)

        # 坑4：可能会出现多窗口，所以要注意切换
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        raw = self.driver.execute_script("return JSON.stringify(performance.timing)")
        print(raw)
        j = json.loads(raw)
        print(j["connectStart"])

        # phone = (By.ID, 'phone-number')
        #
        # # html定位的常见问题，元素可以找到的时候，不代表可以交互，需要用显式等待
        # WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(phone))
        # self.driver.find_element(*phone).send_keys("15600534760")

    #底层方法滚动
    def test_uiselector(self):
        #找到一个可滚动的控件UiScrollable调用一个可滚动的方法UiSelector.scrollable(true)滑倒到特定标志的文本UiSelector().text("WebView")
        scroll_to_elemment = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector.scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("一只花蛤").instance(0));')
        self.driver.find_element(*scroll_to_elemment).click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,"new UiScrollable(new UiSelector.scrollable(true).instance(0)).scrollIntoView(new UiSelector().text('一只花蛤').instance(0));").click()

    def teardown(self):
        time.sleep(3)
        self.driver.quit()





