from selenium import webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get(r'http://8.129.91.152:8765/ ')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element_by_xpath('//*[@class="no-border special-color"]').click()
driver.find_element_by_xpath('//*[@class="form-control reg-mobile phoneNum"]').send_keys('13864188512')

time.sleep(15)
driver.find_element_by_xpath('//*[@class="btn btn-success left reget-mobileCode"]').click()
time.sleep(1)

text = driver.find_element_by_xpath('//*[@class="layui-layer-content"]')
str = text.text
aaa = str[len(str)-4:]
driver.find_element_by_xpath('//*[@name="code"]').send_keys(aaa)


driver.find_element_by_xpath('//*[@type="password"]').send_keys('qwer1234')
driver.find_element_by_xpath('//*[@name="agree"]').click()
driver.find_element_by_xpath('//*[@class="btn btn-special"]').click()

time.sleep(5)
# driver.close()
driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]').click()  #系统自动分配



# a = driver.window_handles
# driver.switch_to.window(a[1])
time.sleep(5)
driver.find_element_by_xpath("//*[@src = '/Public/frontend/images/personal_center/identity_iden_no.png' and @title='实名认证']").click()

driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/ul/li[4]/a').click()


driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[1]/input').send_keys('qwer1234') #原始密码
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[2]/input').send_keys('qwe12344') #新密码
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[3]/input').send_keys('qwe12344') #确认新密码

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[5]/button[1]').click()  #点击确定

time.sleep(5) #修改完密码后休息5秒

#实名认证
driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/ul/li[1]/a').click()
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[1]/div/input').send_keys("蔚超慧")
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[2]/div/input').send_keys('150925199801265214') #因为它需要我输入正确的身份证号，就没真的进行
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[3]/div/button').click()


#添加银行卡
driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[2]/a').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/a').click()  #点击添加银行卡




# driver.quit()















