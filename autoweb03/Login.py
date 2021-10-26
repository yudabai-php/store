
'''
    整合数据和页面的操作逻辑：
'''
from ddt import ddt
from ddt import data
from ddt import unpack
from unittest import TestCase
import time
from Login1 import InitPage
from Login2 import LoginOperation
from Login3 import Write_excel
from selenium import webdriver


n = 1

@ddt
class TestHkr(TestCase):
    # 在用例执行前执行
    def setUp(self) -> None:
        # 调用浏览器完成实际操作
        self.driver = webdriver.Chrome()
        self.driver.get(r"http://localhost:8081/HKR/index.jsp")
        self.driver.maximize_window()
    # 在用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()


    # 登陆成功的用例
    @data(*InitPage.Login_Success_data)
    # @unpack
    def testHkrLoginSuccess(self,testdata):
        #  提取三项数据
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]
        loginOper = LoginOperation(self.driver)

        #  完成登陆的三项操作
        loginOper.login(username,password)
        time.sleep(3)
        # 获取实际结果
        data = loginOper.getSuccessReslt()
        time.sleep(2)

        global n
        table = Write_excel(r'D:\Python\Pythondaim\autoweb03\HKR.xlsx')
        if data == expect:
            table.write(n + 1, 4, 'pass')

        else:
            table.write(n + 1, 4, 'fail')
        n += 1

        # 断言
        self.assertEqual(data,expect)
        # 把结果直接会写到excel表里，xlwt写


  # 登陆成功的用例
  #   @data(*InitPage.Login_error_data)
  #   def testHkrLoginError(self,testdata):
  #       #  提取三项数据
  #       username = testdata["username"]
  #       password = testdata["password"]
  #       expect = testdata["expect"]
  #       loginOper = LoginOperation(self.driver)
  #
  #       #  完成登陆的三项操作
  #       loginOper.login(username,password)
  #       time.sleep(3)
  #       # 获取实际结果
  #       data = loginOper.getErrorResult()
  #
  #       # 断言
  #       self.assertEqual(data,expect)
