'''
    任务1：
        自动化刷抖音
    任务2：
        新浪微博登陆自动化框架写出来。
'''

import time
from appium import webdriver

remote = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.sina.weibo",
  "appActivity": "com.sina.weibo.SplashActivity"
}

driver = webdriver.Remote(remote, param)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
el1.click()


time.sleep(3)
el2 = driver.find_element_by_id("com.sina.weibo:id/titleBack")
el2.click()


time.sleep(4)
el3 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_phone").send_keys("18731516477")
# el3.send_keys("18731516477")


el4 = driver.find_element_by_id("com.sina.weibo:id/tv_login_view_resent")
el4.click()



el5 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_sms")
el5.send_keys()
time.sleep(10)

el6 = driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol")
el6.click()


el9 = driver.find_element_by_id("com.sina.weibo:id/btn_login_view_sms")
el9.click()














