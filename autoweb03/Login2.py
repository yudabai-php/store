
import time

class LoginOperation:

    # 将用例传过来的driver变成全局driver
    def __init__(self,driver):
        self.driver = driver

    # login只做登陆的三个操作
    def login(self,username,password):

        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

        time.sleep(2)

    #  获取成功的实际结果
    def getSuccessReslt(self):
        return self.driver.title

    # 获取失败的实际结果
    def getErrorResult(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text