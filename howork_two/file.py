'''python文件读写分为三步
1. open   打开文件，并且返回文件操作对象
2.read    将文件内容读取到内存
3 write   将指定内容写入文件
4 close   关闭文件'''

# 文件打开时，需指定文件路径、打开方式，windows文件路径如果是
# “E:\person_practice\python\test.txt”，需要把"\"做转移，或者改成："E:/person_practice/python/test.txt"
'''
 f = open("E:\\person_practice\\python\\test.txt","r")   #打开文件
 fr = f.read()                                           #读取文件
 print(fr)
'''

'''
打开方式分为r、w、a三种方式 ，【+】表示可以同时读写
r　　只读，默认模式
w　  只写，不可读，若文件不存在则创建，若存在，则删除内容，写入新内容
a　　只追加，不可读，若文件不存在则创建，存在则追加新内容
r+　　可读、可写、可追加，若文件不存在，则报错
w+　　可读、可写，若文件存在，内容会被清空，可读新写入的内容
a+　　可读、可写、可追加，若文件存在，则追加新内容，读时默认指针在文件末尾，若需读取整个文件，
需把指针归零【f.seek(0)】
此种方式打开文件，需要在使用结束后及时关闭文件，可以使用【with】方法来解决：
with open("F:\\python_scripts\\py\\test.txt ","r") as fr:　　#以r形式打开文件 
　　for line in fr:　　　　　　　　　　　　　　　　　　            #一行一行读取 
　　print(line)
'''

# 实例
# # 1.打开文件
# file = open("E:/01.txt")
# print(file)
# # 2.读取,显示行数
# text = file.read()
# print(text)
# print(len(text))
# print(" - " * 10) #打印分割线
# # 3.关闭文件
# file.close()


# 打开文件的方式
"""
如果open函数只传第一个函数，那么函数默认为只读权限
"""
# 写入文件

# 打开
# file = open("E:/01.txt","w")# w写入会覆盖原有内容。a是追加在原有内容后面
# # 写入
# file.write("cat")
#
# # 关闭
# file.close()
#
# readline 方法.查看单行
#
# file = open("E:/01.txt")
# text = file.readline()
# print(text) #查看单行
#
# file.close()


# 多行读取
#  readline 方法.查看单行
# # #
# file = open("E:/01.txt")
# while True:
#
#     text = file.readline()
#     if not text:
#         break
#     print(text) #查看单行
# file.close()


# 文件复制

# # 小文件复制
# # 打开
# file1 = open("E:/01.txt")#源文件
# file2 = open("E:/02.txt","w")#目标文件
#
# # 2.读写
# text = file1.read()
# file2.write(text)
# # 3关闭文件
#
# file1.close()
# file2.close()


# 大文件复制

# # 打开
# file1 = open("E:/01.txt")#源文件
# file2 = open("E:/02.txt","w")#目标文件

# 2.读写
# while True:
#     text = file1.readline()
#     # 判断是否读取到内容
#     if not text:
#         break
#     file2.write(text)
# # 3关闭文件
#
# file1.close()
# file2.close()


# 文件目录的常用管理操作
# os 模块中的方法
"""
1.rename    重命名
2.remove    删除
3.listdir      查看目录下文件
4.mkdir         创建目录
5.rmdir            删除目录
6.getcwd            获取当前目录
7.chdir             修改当前目录
8.path.isdir        判断是否为文件
"""
# -------------------------------------------------------------------------
# 异常的概念:如果python遇到一个错误,会停止程序的执行,并提示一些错误信息
# 程序停止执行并提示错误信息,我们称之为:抛出异常


# 捕获异常
# try:
#     # 尝试执行的代码
# except:
#     # 出现错误的处理

# 实例
# try:
#     num = int(input("请输入一个整数"))
# except:
#     print("请输入正确的整数")
# print("- "* 50)


# 错误类型捕获:针对不同类型的错误给出不同类型的相应
# 当python解释器抛出异常后,最后一行错误信息的第一个单词,就是错误类型
# try:
#     # 实例  提示用户书如一个整数
#     num = int(input("请输入整数:"))
#     # 使用 8 除以用户输入的整数并且输出
#     result = 8 / num
#
#     print(result)
# except ZeroDivisionError:
#     print("除零错误")
# except ValueError:
#     print("请输入正确的整数!")


# 捕获位置错误


# try:
#     # 实例  提示用户书如一个整数
#     num = int(input("请输入整数:"))
#     # 使用 8 除以用户输入的整数并且输出
#     result = 8 / num
#
#     print(result)
# except ValueError:
#     print("请输入正确的整数!")
# except Exception as result:
#     print("未知错误 %s" % result)


# 异常捕获完整语法
# else   只要尝试成功就执行else
# finally  无论是否尝试成功.都执行

# try:
#     # 实例  提示用户书如一个整数
#     num = int(input("请输入整数:"))
#     # 使用 8 除以用户输入的整数并且输出
#     result = 8 / num
#
#     print(result)
# except ValueError:
#     print("请输入正确的整数!")
# except Exception as result:
#     print("未知错误 %s" % result)
# else:
#     print("尝试成功")
# finally:
#     print("无论是否出现错误都会执行的代码")
#
# print("- "* 50)



# 主动抛出raise异常
# 创建异常对象
# 抛出异常对象

# def input_password():
#     # 提示用户输入密码
#     pwd = input("请输入密码:")
#     # 判断密码长度>=8,返回用户输入的密码
#     if len(pwd) >= 8:
#         return pwd
#     # 如果<=8主动抛出异常
#     print("主动抛出异常")
#
#     ex = Exception("密码长度不够")
# #     抛出异常
#     raise ex
# # 提示用户输入密码
# try:
#     print(input_password())
# except Exception as result:
#     print(result)



# csv
# csv是Comma-Separated Values的缩写，是用文本文件形式储存的表格数据
# 1.读文件
# 第一种方法使用reader函数，接收一个可迭代的对象（比如csv文件），能返回一个生成器，就可以从其中解析出csv的内容：比如下面的代码可以读取csv的全部内容，以行为单位

import csv

# with open("test.csv","r",encoding="utf-8")as f:
#     reader = csv.reader(f)
#     rows = [row for row in reader]
# print(rows)


# 要提取其中某一列，可以用下面的代码
# with open("test.csv", "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     column = [row[1] for row in reader]
#
# print(column)

# 注意从csv读出的都是str类型

# 第二种方法是使用DictReader，和reader函数类似，接收一个可迭代的对象，能返回一个生成器，但是返回的每一个单元格都放在一个字典的值内，而这个字典的键则是这个单元格的标题（即列头）。用下面的代码可以看到DictReader的结构

# with open("test.csv", "r", encoding = "utf-8") as f:
#     reader = csv.DictReader(f)
#     column = [row for row in reader]
#
# print(column)

# 如果我们想用DictReader读取csv的某一列，就可以用列的标题查询
# with open("test.csv", "r", encoding = "utf-8") as f:
#     reader = csv.DictReader(f)
#     column = [row['Name'] for row in reader]
#
# print(column)


# 写文件
# 追加

# row = ['5','hanmeimei','23','81']
# out = open("test.csv","a",newline="")
# csv_writer = csv.writer(out,dialect="excel")
# csv_writer.writerow(row)
#




# python 中的json
"""
JSON 的全称是 JavaScript Object Notation，即 JavaScript 对象符号，它是一种轻量级的数据交换格式。JSON 的数据格式既适合人来读写，也适合计算机本身解析和生成。最早的时候，JSON 是 JavaScript 语言的数据交换格式，后来慢慢发展成一种语言无关的数据交换格式，这一点非常类似于 XML。
JSON 主要有如下两种数据结构：
由 key-value 对组成的数据结构。这种数据结构在不同的语言中有不同的实现。例如，在 JavaScript 中是一个对象；在 Python 中是一种 dict 对象；在 C 语言中是一个 struct；在其他语言中，则可能是 record、dictionary、hash table 等。
有序集合。这种数据结构在 Python 中对应于列表；在其他语言中，可能对应于 list、vector、数组和序列等。
JSON 类型	Python 类型
对象（object）	字典（dict）
数组（array）	列表（list）
字符串（string）	字符串（str）
整数（number(int)） 	整数（int）
实数（number(real)）	浮点数（float）
true	True
false	False
null 	None
"""

# 常用有2个方法，也是最基本的使用方法：
#

# import codecs
# import json
# test_dict = {'a':1, 'b':2}
#
# #把字典转成json字符串
# json_text = json.dumps(test_dict)
#
# #把json字符串保存到文件
# #因为可能json有unicode编码，最好用codecs保存utf-8文件
# with codecs.open('1.json', 'w', 'utf-8') as f:
#     f.write(json_text)




#

# import json
# import codecs
#
# # 从文件中读取内容
# with codecs.open('1.json', 'r', 'utf-8') as f:
#     json_text = f.read()
#
# # 把字符串转成字典
# json_dict = json.loads(json_text)



# 1、dumps：把字典转成json字符串import json
# import json
# import codecs
# text_dict = {'a':1,'b':2}
# #把字典转成json字符串并写入到文件
# with codecs.open("1.json",'w','utf-8')as f:
#     json.dump(text_dict,f)


# 2、loads： 把json字符串转成字典
# import json
# import codecs
#
# # 从json文件读取json字符串到字典
# with codecs.open('1.json', 'r', 'utf-8') as f:
#     json_dict = json.load(f)
