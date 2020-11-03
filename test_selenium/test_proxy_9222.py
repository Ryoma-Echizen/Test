from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--windows-size=1280,1696")
#使用已经存在的chrome进程
options.debugger_address='127.0.0.1:9222'
driver = webdriver.Chrome(options=options)
print(driver.title)