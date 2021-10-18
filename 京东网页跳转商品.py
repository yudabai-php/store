from selenium import webdriver
from time import sleep

dirver = webdriver.Chrome()

dirver.get("https://www.jd.com/")

dirver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_c' and @type='text'and @id='key']").send_keys("苹果13pro")

dirver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a' and @class='button']").click()

sleep(2)
dirver.find_element_by_xpath("//*[@src='//img14.360buyimg.com/n7/jfs/t1/205226/20/9809/112872/615e991fE2cecdd41/db42acdbae68b709.jpg']").click()























