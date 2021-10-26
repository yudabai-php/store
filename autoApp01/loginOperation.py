# 操作类
import time
class Operation:

    def __init__(self, driver):
        self.driver = driver

    def successfulOperation(self, username):
        time.sleep(2)
        # 点击同意并继续
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]").click()
        # 点击登录
        time.sleep(2)
        self.driver.find_element_by_id("com.sina.weibo:id/titleBack").click()
        # 输入手机号
        time.sleep(2)
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_phone").send_keys(username)
        # 点击获取验证码
        time.sleep(2)
        self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_resent").click()
        # 同意协议
        time.sleep(20)
        self.driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol").click()
        # 登录微博
        time.sleep(15)
        self.driver.find_element_by_id("com.sina.weibo:id/btn_login_view_sms").click()
        # 点击我
        self.driver.find_element_by_accessibility_id("我").click()


    def successful_result(self):
        return self.driver.find_element_by_xpath('//*[@class= "android.widget.TextView"]').text




