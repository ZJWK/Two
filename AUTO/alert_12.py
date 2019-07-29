'''
1、弹窗
selenium提供switch_to_alert方法：捕获弹出对话框（可以定位alert、confirm、prompt对话框）

switch_to_alert()    --定位弹出对话框
text()               --获取对话框文本值
accept()             --相当于点击“确认”
dismiss()            --相当于点击“取消”
send_keys()          --输入值（alert和confirm没有输入对话框，所以就不用能用了，只能使用在prompt里）

'''

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("file:///D:/work/AUTO_test/Two/AUTO/alert.html")
driver.find_element_by_id("alert").click()
driver.implicitly_wait(3)

# 获取alert对话框
kuang = driver.switch_to_alert()
sleep(2)
kuang.accept()

# 获取confirm窗口
driver.find_element_by_id("confirm").click()
confirm_ele = driver.switch_to_alert()

sleep(2)
confirm_ele.dismiss()


# 获取prompt窗口
driver.find_element_by_id("prompt").click()
sleep(2)

prompt_ele = driver.switch_to_alert()
sleep(2)
print(prompt_ele.text)
prompt_ele.send_keys("hello,python")
sleep(3)
print(prompt_ele.text)
sleep(1)
prompt_ele.accept()
driver.quit()





