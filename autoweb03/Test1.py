'''
    修改今日评价、修改个人信息、修改头像
    类：只进行逻辑操作
'''
from selenium.webdriver.support.select import Select
import  time

class  newUsername:

    def __init__(self,dirver):
        self.dirver = dirver

    #注册登录需要输入的东西
    def write(self,username,name,password,pasword,age,sex,office,youxiang,phone,address):
        self.dirver.find_element_by_xpath('//*[@id="loginname"]').send_keys(username)
        time.sleep(1)
        self.dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[2]').send_keys(name)
        time.sleep(1)
        self.dirver.find_element_by_xpath('//*[@id="pwd"]').send_keys(password)
        time.sleep(1)
        self.dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[4]').send_keys(pasword)
        time.sleep(1)

        self.dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()
        time.sleep(2)

        self.dirver.find_element_by_xpath('//*[@id="valid_age"]').send_keys(age)
        time.sleep(2)

        ele = self.dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/select[1]')
        st = Select(ele)
        st.select_by_value(sex)
        time.sleep(2)

        ell = self.dirver.find_element_by_xpath('//*[@id="classname"]')
        ss = Select(ell)
        ss.select_by_value(office)
        time.sleep(2)
        self.dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[3]').click()
        time.sleep(2)
        self.dirver.find_element_by_xpath('//*[@id="reg_mail"]').send_keys(youxiang)
        time.sleep(2)
        self.dirver.find_element_by_xpath('/html/body/form/fieldset[3]/input[2]').send_keys(phone)
        time.sleep(2)
        self.dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[3]/textarea').send_keys(address)
        time.sleep(2)
        self.dirver.find_element_by_xpath('//*[@id="btn_reg"]').click()
        time.sleep(2)
        self.dirver.find_element_by_xpath('/html/body/div[2]/div[3]/a').click()
        time.sleep(2)

    def getSuccess_result(self):
        return self.dirver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]').text

    def getError_result(self):
        return  self.dirver.find_element_by_xpath('/html/body/div[2]/div[2]').text








