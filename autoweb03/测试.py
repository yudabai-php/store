from selenium import webdriver

driver =  webdriver.Chrome()


driver.get(r"http://localhost:8081/HKR/index.jsp")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("1234567")
driver.find_element_by_xpath("//*[@id='submit']").click()

driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[1]/div').click()








