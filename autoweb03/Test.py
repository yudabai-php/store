from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Test1 import newUsername
from Test2 import InitData
import time
from selenium.webdriver.support.select import Select

'''
    成功的用例
    失败的用例
'''
@ddt
class TestLogin(TestCase):
    #在每个测试用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8081/HKR/register.jsp")
        self.driver.maximize_window()

    # 在每个用例执行后关闭
    def tearDown(self) -> None:
        self.driver.quit()

    @data(*InitData.Login_success_data)
    # def write(self, usernmae, name, password, pasword, age, sex, office, youxiang, phone, address):
    def testLoginSuccess(self,testdata):
        username = testdata["username"]
        name = testdata["name"]
        password = testdata["password"]
        pasword  = testdata["pasword"]
        age = testdata["age"]
        sex = testdata["sex"]
        office = testdata["office"]
        youxiang = testdata["youxiang"]
        phone = testdata["phone"]
        address = testdata["address"]
        expect = testdata["expect"]

        time.sleep(3)

        Login = newUsername(self.driver)
        Login.write(username, name, password, pasword, age, sex, office, youxiang, phone, address)
        result =Login.getSuccess_result()
        time.sleep(3)
        self.assertEqual(result,expect)

    @data(*InitData.Login_success_data)
    # def write(self, usernmae, name, password, pasword, age, sex, office, youxiang, phone, address):
    def testLoginError(self, testdata):
        username = testdata["username"]
        name = testdata["name"]
        password = testdata["password"]
        pasword = testdata["pasword"]
        age = testdata["age"]
        sex = testdata["sex"]
        office = testdata["office"]
        youxiang = testdata["youxiang"]
        phone = testdata["phone"]
        address = testdata["address"]
        expect = testdata["expect"]
        time.sleep(3)

        Login = newUsername(self.driver)
        Login.write(username, name, password, pasword, age, sex, office, youxiang, phone, address)
        result = Login.getError_result()
        time.sleep(3)
        self.assertEqual(result, expect)























