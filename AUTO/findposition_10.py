'''
一、定位元素（选择定位的元素必要唯一）
1、通过js前端找到对应的id来搜索  find_element_by_id()
2、通过name来搜索  find_element_by_name()     id、name、和class一般在网页都至少会有其中的一种
3、通过class来搜索   find_element_by_class_name()

4、通过tag name来定位  find_element_by_tag_name()    ----一般不适用，因为大多数情况tag都不唯一
5、通过link text来定位[超链接]  find_element_by_link_text()      ---------
'''


'''
定位到元素后的方法：
clear()---清空
send_keys()---输入
back()---后退页面
maximize_window()---最大化窗口
click()---点击事件，点击按钮，超链接
submit()---提交表单
'''
# eg:通过id查找
# from selenium import webdriver
# driver = webdriver.Chrome()
# # 跳转到具体的网页地址
# driver.get("https://www.baidu.com")
# print(driver.title)
# # 选中输入框，输入
# driver.find_element_by_id("kw").send_keys("慕课网")
# # 选中按钮，点击按钮“百度一下”
# driver.find_element_by_id("su").click()

# eg:通过name查找
# from selenium import webdriver
# driver = webdriver.Chrome()
# # 跳转到具体的网页地址
# driver.get("https://www.baidu.com")
# print(driver.title)
# # 选中输入框，输入
# driver.find_element_by_name("wd").send_keys("慕课网")
# # 选中按钮，点击按钮“百度一下”
# driver.find_element_by_id("su").click()

# eg:通过class查找
'''
from selenium import webdriver
driver = webdriver.Chrome()
# 跳转到具体的网页地址
driver.get("https://www.baidu.com")
print(driver.title)
# 选中输入框，输入
driver.find_element_by_class_name("s_ipt").send_keys("慕课网")
# 选中按钮，点击按钮“百度一下”
driver.find_element_by_id("su").click()
'''


# 通过find_element_by_link_text()查找   超链接
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
driver.get("https://www.imooc.com")
print(driver.title)
sleep(3)   # 设置睡眠时间2s
# driver.find_element_by_link_text("地图").click()
#模糊查询
driver.find_element_by_partial_link_text("课程")
