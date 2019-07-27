# 模拟用户行为
'''
1、需求：需要模拟鼠标操作才能进行的情况，比如单击、双击、鼠标右键、拖拽等操作
2、解决办法：selenium 提供了一个类来处理这类事件：selenium.webdriver.common.action_chains.ActionChains(driver)
3、脚本：from selenium.webdriver.common.action_chains import AchtionChains
4、原理：调用ActionChains不会立即执行，而是将所有的操作顺序放在一个队列里，当调用perform()方法时，队列中的事件会被依次执行
5、写法：支持链式写法和分步写法:
ActionChains(driver).click(ele).perform()


6、键盘和鼠标方法列表：
（1）perform()执行列表中所有的操作
（2）click(on_element=None)　　单击鼠标左键
（3）context_click(on_element=None)　　单击鼠标右键
（4）double_click(on_element=None)　　双击鼠标左键
（5）move_to_element(to_element)　　移动鼠标到某个元素上
（6）ele.send_kends(keys_to_send)　　发送某个词到当前焦点的元素
7、不常用的方法列表：
（1）click_and_hold(on_element=None)　　点击鼠标左键不松开
（2）release(on_element=None)　　在某个元素位置松开鼠标左键
（3）key_down(value,element=None)　　按下键盘上的某个键
（4）key_up(value,element=None)　　松开键盘上的某个键
（5）drag_and_drop(source,target)　　拖拽到某个元素然后松开
（6）drag_and_drop_by_offset(source,xoffset,yoffset)　　拖拽到某个坐标然后松开
（7）move_by_offset(xoffset,yoffset)　　鼠标从当前位置移动到某个坐标
（8）move_to_element_with_offset(to_element,xoffset,yoffset)　　移动到距某个元素（左上角坐标）多少距离的位置　　
'''


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains

url = 'https://www.imooc.com'
broswer = webdriver.Firefox()
broswer.get(url)
sleep(3)
print(broswer.title)
# 定位鼠标移动到上面的元素
positionTest = broswer.find_element_by_css_selector("div.item:nth-child(6) > a:nth-child(1) > span:nth-child(1)")
ActionChains(broswer).move_to_element(positionTest).perform()
sleep(3)
# 选中子菜单
positionAutotest = broswer.find_element_by_css_selector("div.submenu:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(9)")
positionAutotest.click()



