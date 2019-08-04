import unittest
import time
import HTMLTestRunner
class Test(unittest.TestCase):
    def setUp(self):
        print("Test.setUp")


    def test_One(self):
        u"test one案例说明，属于Test类"
        print("Test.test_One")


    def tearDown(self):
        print("Test.tearDown")

class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1.setUp")

    def test_One(self):
        print("Test1.test_One")

    def tearDown(self):
        print("Test1.tearDown")

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_One'))
    suite.addTest(Test1('test_One'))

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    filename = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    print(filename)
    fp = open("./"+filename+"_report.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"demo 测试报告", description=u"测试用例执行情况")
    runner.run(suite)
    fp.close()
