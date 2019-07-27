'''
1、为什么需要设置等待时间：网页需要加载对应的资源，页面渲染，窗口处理等
2、自动化测试常用的等待时间
（1）强制等待：
from time import sleep
sleep(3)    //强制等待3s再执行下一步，缺点是不管资源是不是完成，都必须等待

（2）
隐形等待：
driver.implicitly_wait(10)  隐形等待 最长等待10s
隐性等待对整个driver的周期都起作用，所以只要设置一次即可。
隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，
则执行下一步，否则一直等到时间截止。


(3)显性等待
WebDriverWait()会配合until()和until_not()方法一起使用，根据判断条件而进行灵活进行处理时间等待问题，
他会不断的根据你设定的条件去判断，直到超过你设置的等待时间，如果设置的条件满足，然后进行下一步操作，
如果没有满足会报一个'selenium.common.exceptions.TimeoutException: Message: '错误，
使用WebDriverWait首先需要导入from selenium.webdriver.support.ui import WebDriverWait模块
'''


# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(30) # 最长等待30秒
# driver.get("http://www.baidu.com")
# print (driver.current_url)
# driver.quit()
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)  #这里设置智能等待10s
# driver.get('http://news.baidu.com')
# print (driver.title)
# driver.quit()



# from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# try:
# #为了更好的对比效果，首先我们设置了一个存在的元素，然后在去找一个不存在的元素，同样设置了10s的等待时间
# #kw元素存在时
#     print(datetime.now())  #until 也属于WebDriverWait,代表一直等待,直到某元素可见，until_not与其相反，判断某个元素直到不存在
#     element = WebDriverWait(driver,5).until(
#     EC.presence_of_element_located((By.ID, "kw"))
# )  #presence_of_element_located主要判断页面元素kw在页面中存在。
# #kw111元素不存在时
#     print(datetime.now())
#     element = WebDriverWait(driver,10).until_not(
#     EC.presence_of_element_located((By.ID, "kw111"))
# )
#
# finally:
#     print(datetime.now())
#     driver.quit()
