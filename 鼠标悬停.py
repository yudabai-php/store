from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

driver= webdriver.Chrome()

driver.get("https://item.jd.com/")
driver.maximize_window()

ele = driver.find_element_by_link_text("我的京东")

ac = ActionChains(driver)

ac.move_to_element(ele).perform()
