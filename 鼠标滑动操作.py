from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

driver= webdriver.Chrome()

driver.get(r"D:/a_py培训/py自动化测试/PY/Python自动化/day01/练习的html/滑动验证/mousedrag.html")
driver.maximize_window()

ele = driver.find_element_by_xpath('//*[@id="box"]/div[3]')

ac = ActionChains(driver)

ac.click_and_hold(ele).move_by_offset(300,0).perform()  # 滑动

ac.release() # 释放


















