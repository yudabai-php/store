from appium import webdriver
import  time

remote = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}

driver = webdriver.Remote(remote,param)
while True:
  # t = 10
  # if t > 0:
    time.sleep(5)
    start_x = 500
    start_y = 1400
    distance = 1000
    driver.swipe(start_x,start_y,start_x,start_y - distance)
    # t = t + 1
  # else:
  #   break













