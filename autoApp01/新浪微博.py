from appium import webdriver

remote = "127.0.0.1:4723/wd/hub"


param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.sina.weibo",
  "appActivity": "com.sina.weibo.SplashActivity"
}

driver = webdriver.Remote(remote,param)

