# unittest框架说明
# https://docs.python.org/2/library/unittest.html
# unitest = TestCase + TestResult  执行用例+结果


# 自己写的py文件，不能用unittest.py命名，不然会找不到TestCase

# 单元测试框架unitest入门：

#  -*- coding: utf-8 -*-    #防止中文出现乱码
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2016-7-27
@author: Jennifer
Project:使用unittest框架编写测试用例思路
'''
# 3.导入unittest模块
import unittest
import HTMLTestRunner
import time


# 4.定义测试类，父类为unittest.TestCase。
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。setUp和tearDown方法在每个测试方法时都会被调用。
# 可继承unittest.TestCase的各种断言方法。
class Test(unittest.TestCase):

    # 5.定义setUp()方法用于测试用例执行前的初始化工作。
    # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    # 注意，输入的值为字符型的需要转为int型
    def setUp(self):
        self.number = input('Enter a number:')
        self.number = int(self.number)

    # 6.定义测试用例，以“test_”开头命名的方法
    # 注意，方法的入参为self
    # 可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    # 可定义多个测试用例
    # 最重要的就是该部分
    def test_case1(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg='Your input is not 10')     #断言

    def test_case2(self):
        print(self.number)
        self.assertEqual(self.number, 20, msg='Your input is not 20')

    # @unittest.skip('暂时跳过用例3的测试')
    # def test_case3(self):
    #     print(self.number)
    #     self.assertEqual(self.number, 30, msg='Your input is not 30')

    # 7.定义tearDown()方法用于测试用例执行之后的善后工作。
    # 注意，方法的入参为self
    def tearDown(self):
        print('Test over')


# 8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__ == '__main__':
    # 8.1执行测试用例方案一如下：
    # unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
    # 执行顺序是命名顺序：先执行test_case1，再执行test_case2
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(Test('test_case2'))
    suite.addTest(Test('test_case1'))
    # 这里的verbosity是一个选项,表示测试结果的信息复杂度，有三个值
    # 0(静默模式): 你只能获得总的测试用例数和总的结果比如,总共100个失败20成功80
    # 1(默认模式): 非常类似静默模式,只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
    # 2(详细模式): 测试结果会显示每个测试用例的所有相关的信息,并且你在命令行里加入不同的参数可以起到一样的效果
    # runner = unittest.TextTestRunner(verbosity=1)
    # runner.run(suite)
    filename = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    print(filename)
    fp = open("./" + filename + "_report.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"demo 测试报告", description=u"测试用例执行情况")
    runner.run(suite)
    fp.close()


'''
#8.2执行测试用例方案二如下：
#8.2.1先构造测试集
#8.2.1.1实例化测试套件
    suite=unittest.TestSuite()
#8.2.1.2将测试用例加载到测试套件中。
#执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
    suite.addTest(Test('test_case2'))
    suite.addTest(Test('test_case1'))
#8.2.2执行测试用例
#8.2.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(suite)
'''

'''
#8.3执行测试用例方案三如下：
#8.3.1构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
#执行顺序同方案一：执行顺序是命名顺序：先执行test_case1，再执行test_case2
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#8.3.2执行测试用例
#8.3.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.3.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)   
'''

