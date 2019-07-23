# selenium下载地址：https://pypi.org/project/selenium/
# 在selenium安装文件下shift+右键，然后输入命令
# python setup.py install安装
# 判断selenium是否安装成功：(在执行该命令时记得切换到python的安装根目录下)pip list  或者在python环境下 import selenium,如果没有报错的话
# 就代表成功安装了selenium
# selenium验证安装：将浏览器驱动复制到Python安装路径
# 谷歌浏览器驱动下载地址:https://chromedriver.storage.googleapis.com/index.html

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://baidu.com")


# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()
# sleep(3)
# driver.close()


'''
前端知识讲解：

'''
