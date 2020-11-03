from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver : WebDriver
    _black_list =[
        (By.ID,'tv_agree'),
        (By.XPATH,'//*[@text="确定"]'),
        (By.ID, 'image_cancel'),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 0
    _error_count = 3
    def __init__(self,driver:WebDriver = None):
        self._driver = driver
    #当有广告、评价等弹框时，进行异常流程处理

    def find(self, locator, value : str = None):
        try:
            element = self._driver.find_element(*locator) if isinstance(locator,tuple) else self._driver.find_element(locator,value)
            #如果成功，清空错误计数
            self._error_count = 0
            return element
        except Exception as e:
            #如果次数太多，则退出异常处理，直接报错
            if self._error_count > self._error_max:
                raise e
            #记录一直异常的次数
            self._error_count += 1
            #对黑名单里的弹框进行处理
            for element in self._black_list:
                elements = self._driver.find_elements(*element)
                if len(elements) > 0 :
                    elements[0].click()
                    #继续寻找原来正常的控件
                    return self.find(locator,value)
                #如果黑名单也没有
                raise e
                # self._driver.back()
                # self._driver.back()
                # self.find(locator,value)

    def get_toast(self):
        return self.find(By.XPATH,'//*[@class="android.widget.Toase"]').text

    def text(self,key):
        return (By.XPATH,'//*[text="%s"]' % key)

    def find_by_text(self,key):
        return self.find(self.text(key))

