from selenium import webdriver

dirver = webdriver.Chrome()

dirver.get("https://www.suning.com/")
dirver.implicitly_wait(3)


dirver.find_element_by_xpath("//*[@id='searchKeywords' and @class='search-keyword']").send_keys("苹果13pro")


dirver.find_element_by_xpath("//*[@id='searchSubmit' and@class='search-btn btn-new']").click()


dirver.find_element_by_xpath("//*[@src='//image.suning.cn/uimg/pcms/label05/653232322684286733950000_11.png']").click()

a = dirver.window_handles

dirver.switch_to.window(a[1])

dirver.find_element_by_xpath("//*[@id='addCart' and @class='btn-orange-buy outline-blind']").click()


