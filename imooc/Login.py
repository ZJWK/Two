from selenium import webdriver
from  time import sleep
import unittest
import HTMLTestRunner

class Login(unittest.TestCase):
    def setUp(self):
        print("开始测试")
        self.driver = webdriver.Firefox()
        self.url = "https://www.imooc.com"
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        print("测试结束")
        pass

    def test_login(self):
        u"登录测试用例"
        driver = self.driver

