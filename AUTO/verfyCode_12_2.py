'''
# 破解验证码的常用思路：
1、绕过
（1）开发测试环境临时关闭验证码
（2）提供一个万能验证码
（3）使用cookie[登录是为了拿cookie，获取登录凭证]
2、破解
（1）OCR识别
（2）AI
'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.imooc.com"
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

driver.get_cookie({"name":"cvde","value":"5d405c02087fb-3"})




# 查找当前登录用户名
name = driver.find_element_by_css_selector(".name")
print(name.text)
# 判断是否登录成功
if name.text == "慕粉3793841":
    print("login success")
else:
    print("login fail")