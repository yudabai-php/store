from  selenium import webdriver


dirver = webdriver.Chrome()

dirver.get(r"D:/a_py培训/py自动化测试/PY/Python自动化/day01/练习的html/弹框的验证/dialogs.html")

dirver.maximize_window()

dirver.find_element_by_xpath("//*[@id='alert']").click()


dirver.find_element_by_xpath("//*[@id='confirm']").click()