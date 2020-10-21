import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:

    def setup_method(self):
        browser = os.getenv("browser","").lower()
        print(browser)
        if browser == "phantomjs":
            self.driver = webdriver.PhantomJS()
        elif browser == "firefox":
            self.driver = webdriver.firefox()

        elif browser == 'headless':
            options = webdriver.ChromeOptions()
            #使用headless模式
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1280,1696")
            self.driver=webdriver.chrome(options=options)

        elif browser =='reuse':
            options = webdriver.ChromeOptions()
            # 使用已经存在的chrome进程
            # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
            options.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=options)

        else:
            options = webdriver.ChromeOptions()
            # 使用已经存在的chrome进程
            # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
            # options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        if browser != 'reuser':
            self.driver.get('https://testerhome.com/')

    def wait(self,timeout,location,element):
        WebDriverWait(self.driver,timeout).until(location(element))

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT,'社团').click()
        # todo:显式等待
        #等待该元素可点击
        # WebDriverWait(self.driver).until(lambda x: self.driver.find_elements(element))
        self.driver.find_element(By.LINK_TEXT, '社区').click()
        #todo:隐式等待

    def test_jinshuju(self):
        time.sleep(5)
        self.driver.get('https://testerhome.com/topic/21495')
        submit = (By.CSS_SELECTOR,'.published-form__submit')
        print(self.driver.window_handles)
        #切换至frame
        self.driver.switch_to.frame(0)
        self.wait(10,expected_conditions.element_to_be_clickable(submit))
        self.driver.find_element(By.CSS_SELECTOR,'.published-form__submit').click()

    def test_mtsc2020(self):
        self.driver.get('https://testerhome.com/topic/21805')
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'第六届中国互联网测试开发大会').click()
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.LINK_TEXT,'演讲申请').click()




