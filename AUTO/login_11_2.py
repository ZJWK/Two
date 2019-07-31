from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.imooc.com"
pwd = ""
username = ""
driver = webdriver.Firefox()
driver.get(url)
sleep(3)
login = driver.find_element_by_id("js-signin-btn")
ActionChains(driver).click(login).perform()

# 找登录框并输入账号与密码
sleep(3)
account = driver.find_element_by_name("email")
account.clear()
account.send_keys(username)
pwdP = driver.find_element_by_name("password")
pwdP.clear()
pwdP.send_keys(pwd)

# 点击“记住登录密码”单选框
try:
    auto_login = driver.find_element_by_id("auto-signin").click()

# 查找登录按钮并摁下
    btn = driver.find_element_by_css_selector("input.moco-btn").click()


# 查找用户头像
    sleep(3)
    user_info = driver.find_element_by_css_selector("#header-avator > img:nth-child(1)")
    ActionChains(driver).move_to_element(user_info).perform()
except :
    driver.get_screenshot_as_file("D:\\work\\AUTO_test\\Two\\截图\\登录失败.png")    #截图并保存在该路径下
# 查找当前登录用户名
name = driver.find_element_by_css_selector(".name")
print(name.text)

# 判断是否登录成功
if name.text == "慕粉3793841":
     print("login success")
     driver.get_screenshot_as_file("D:\\work\\AUTO_test\\Two\\截图\\登录成功.png")
else:
    print("login fail")


