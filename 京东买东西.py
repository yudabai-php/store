from selenium import webdriver
from time import sleep

dirver = webdriver.Chrome()

dirver.get("https://www.jd.com/")
dirver.maximize_window()


dirver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_c' and @type='text'and @id='key']").send_keys("阿米洛键盘")

dirver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a' and @class='button']").click()
sleep(3)
dirver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div').click()

a = dirver.window_handles
dirver.switch_to.window(a[1])


dirver.find_element_by_id("InitCartUrl").click()   #添加购物车

dirver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()

dirver.find_element_by_xpath('//*[@id="loginname"]').send_keys("13310238194")

dirver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys("123456")

dirver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[4]/div[3]/div/form/div[5]/div/a').click()













