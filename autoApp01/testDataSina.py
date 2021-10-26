from appium import webdriver
from loginData import testData
from loginOperation import Operation
from ddt import ddt
from ddt import data
import time
from unittest import TestCase

@ddt
class TestMain(TestCase):

    def setUp(self) -> None:
        remote = '127.0.0.1:4723/wd/hub'
        prame = {
            "deviceName": "127.0.0.1:62001",
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "appPackage": "com.sina.weibo",
            "appActivity": "com.sina.weibo.SplashActivity"
        }
        self.driver = webdriver.Remote(remote, prame)

    @data(*testData.successfulData)
    def testsuccess(self, data):
        # 传入数据
        username = data['username']
        expect = data['expect']

        jia = Operation(self.driver)
        # 调用操作方法
        jia.successfulOperation(username)

        # 调用判断方法
        result = jia.successful_result()
        time.sleep(2)
        # 断言
        self.assertEqual(expect, result)



