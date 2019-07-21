# 不同包下的同名文件区分：包名.文件名   eg:package1.a1    package1.a2
'''
import ----导入一个模块
如果想要引用另外一个模块的变量的话，可以以 模块名.变量名的方式引用
'''
# eg1:

# import importr.channge
# print(importr.channge.a)


# 为了在引用其他模块的变量时，可以为导入的模块名取别名
# eg:
# import importr.channge as m
# print(m.a)


'''
第二种导入方式：
from 模块名1 import 变量名/方法/模块名2
eg:
'''
# from importr.channge import a
# print(a)


# import * 代表引用所有
# from importr.channge import *
# print(a)
# print(b)
# print(c)


# 在引用模块中加入内置变量_all_可以只引用模块中我们想引用的东西
# eg:
# from importr.channge import *
# print(a)
# print(b)
# print(c)



# 导入的包的时候都会自动运行旗下包含的_init_.py文件
# 如果在多个文件中需要用到某些参数、模块或者方法的话，可以考虑写在_init_.py文件里
# 注意：1、模块和包是不会被重复导入的
#         2、尽量不要循环引入
# eg：
# import importr
# print(importr.sys.path)

