'''任务1：
    完成除了滑动验证之外的其他的操作。
任务2：
    京东搜索一个商品，点击查看详情。
    苏宁：搜索一个商品，点击商品详情 --> 添加购物车 --> 结算。
'''


#点击跳转页面
from  selenium import  webdriver

dirver = webdriver.Chrome()

dirver.get(r"D:/a_py培训/py自动化测试/PY/Python自动化/day01/练习的html/跳转页面/pop.html")

dirver.maximize_window()

dirver.find_element_by_xpath("//*[@id='goo']").click()


























