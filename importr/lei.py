# 类最基本的作用就是封装
class Student():
    name = 'xiaomin'   # 类变量
    age = 0
    def __init__(self, name, age): #构造函数,用于创建不同属性的对象
    # def __init__(this, name, age):
        # 初始化对象
        self.name = name   # self.name为实列变量   self不是关键字，是可以更改的
        self.age = age
        # print('student')
        # return 'studdent'#构造函数不能随便返回除none 以外的值，否则会报错
    # def print_file(self):     # 类下定义方法时必须要有self
    #     print('name:'+self.name)   #类下使用变量的时候需要加上self
    #     print('age:'+str(self.age))
student = Student('Kate',18)  # 类的实例化 在实例化的时候就会自动运行__init__(self)方法
# student.print_file() # 调用类的方法
# a,b=student.name,student.age
# print(a, b)
print(student.name)
print(Student.name)



