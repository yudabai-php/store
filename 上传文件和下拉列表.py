'''
任务1：
    完成除了滑动验证之外的其他的操作。
任务2：
    京东搜索一个商品，点击查看详情。
    苏宁：搜索一个商品，点击商品详情 --> 添加购物车 --> 结算。
'''





from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"D:/a_py培训/py自动化测试/PY/Python自动化/day01/练习的html/上传文件和下拉列表/autotest.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='accountID']").send_keys("jason")

driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("admin")

driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")

driver.find_element_by_xpath("//*[@id='sexID2']").click()

driver.find_element_by_xpath("//*[@value='spring']").click()

driver.find_element_by_xpath("//*[@value='Auterm']").click()

driver.find_element_by_xpath("//input[@name='file' and @type='file']").send_keys(r"C:\Users\jason\Pictures\景甜.jpg")



















