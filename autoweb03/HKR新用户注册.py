from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

dirver = webdriver.Chrome()
dirver.get(r"http://localhost:8081/HKR/register.jsp")

youxiang = "2291494711@qq.com"

dirver.maximize_window()
dirver.implicitly_wait(3)

dirver.find_element_by_xpath('//*[@id="loginname"]').send_keys("ych")
dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[2]').send_keys("蔚大白")
dirver.find_element_by_xpath('//*[@id="pwd"]').send_keys("123456")
dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[4]').send_keys("123456")

dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()

dirver.find_element_by_xpath('//*[@id="valid_age"]').send_keys("23")

ele = dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/select[1]')
st = Select(ele)
st.select_by_value("男")

ell = dirver.find_element_by_xpath('//*[@id="classname"]')
ss = Select(ell)
ss.select_by_value("安全渗透测试")
time.sleep(2)
dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[3]').click()
time.sleep(3)
dirver.find_element_by_xpath('//*[@id="reg_mail"]').send_keys(youxiang)
time.sleep(2)
dirver.find_element_by_xpath('/html/body/form/fieldset[3]/input[2]').send_keys("13310228888")
dirver.find_element_by_xpath('//*[@id="msform"]/fieldset[3]/textarea').send_keys("内蒙古乌兰察布市凉城县")
dirver.find_element_by_xpath('//*[@id="btn_reg"]').click()
time.sleep(3)
dirver.find_element_by_xpath('/html/body/div[2]/div[3]/a').click()

time.sleep(3)

dirver.quit()




















