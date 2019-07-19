'''
一、面向对象的概述
面向对象是一种描述业务问题、设计业务实体和实体之间关系的方法
二、类和对象
1、类和对象得区别：类是对客观世界中事物得抽象，而对象是类实例化后的实体
   例如：汽车模型就是一个类，制造出来的每辆汽车就是一个对象
2、类的定义：
   （1）python使用class关键字定义一个类，类名的首字母一般要大写：
       例如：

class Student：   #定义了一个Student类
   （2）类的主体由一系列的属性和方法组成
       例如：

class Fruit：                 #定义一个类
    def __init__(self):       #类的构造函数，用于初始化类的内部状态，为类的属性设置默认值
        self.name=name        #定义name属性
        self.color=color      #定义color属性
    def grow（self）：         #定义一个函数，为类的函数，称为方法；它至少有一个参数self
         print（‘Fruit grow’）
3、对象的创建：
   创建对象的过程称为实例化，当一个对象被创建后，包含3个方面的特性：对象的句柄、属性和方法
   对象的句柄：用于区分不同的对象

例如：

if __name__=="__main__"      #当程序作为主程序运行
    fruit=Fruit()            #实例化：创建一个对象，创建了一个Fruit对象
    fruit，grow()            #对象调用grow（）方法
4、类的属性和方法
   （1）类的属性：一般分为公有属性和私有属性，默认情况下所有得属性都是公有的，如果属性的名字以两个下划线开始，就表示为私有属性，没有下划线开始的表示公有属性。 python的属性分为实例属性和静态属性，实例属性是以self为前缀的属性，如果构造函数中定义的属性没有使用self作为前缀声明，则该变量只是普通的局部变量，类中其它方法定义的变量也只是局部变量，而非类的实例属性。

例如：

class Fruit:
    price=0                                        #定义一个类属性
    def __init__(self):                            #构造函数
        self.color="red"                           #实例属性，以self为前缀
        zone="China"                               #局部变量，不以self为前缀
if __name__=="__main__":
    print(Fruit.price)                             #使用类名调用类变量   0
    apple=Fruit()                                  #实例化apple
    print(apple.color)                             #打印apple实例的颜色  red
    Fruit.price=Fruit.price+10                     #将类变量+10
    print("apple's price:",+str(apple.price))      #打印apple实例的price   10
    banana=Fruit()                                 #实例化banana
    print("banana's price:"+str(banana.price))     #打印banana实例的price    10
        注意：python的类和对象都可以访问类属性；类的外部不能直接访问私有属性（属性名以两个下划线开始），当把上面的self.color=color改为self.__color="red"，再次执行print(Fruit.__color)的时候就会报错
    （2）类的方法：类的方法也分为公有方法和私有方法，私有方法不能被模块外的类或者方法调用，也不能被外部的类或函数调用。python利用staticmethon或@staticmethon 修饰器把普通的函数转换为静态方法

class Fruit:
    price=0                             #类变量
    def __init__(self):                 #构造函数
        self.__color="red"              #定义一个私有属性，类的外部不能直接访问
    def getColor(self):                 #类方法
        print(self.__color)             #打印出私有变量

    @staticmenthod                      #使用修饰器静态方法
    def getPrice():                     #定义一个类方法
        print(Fruit.price)              #打印类变量
    def __getPrice():                   #定义私有函数，不能被模块外的类或者方法调用
        Fruit.price=Fruit.price+10      #类变量+10
        print(Fruit.price)
    count=staticmenthod(__getPrice)      #定义静态方法
if __name__=="__main__":
    apple=Fruit()                       #实例化apple
    apple.getColor()         #使用实例私有变量，  red；因为创建了对象apple，所以静态属性price执行一次
    Fruit.count()            #使用列名直接调用静态方法  10
    banana=Fruit()           #实例化  创建banana对象，所以静态属性第三次执行
    Fruit.count()            #实例调用静态方法  20
    Fruit.getPrice()         # 20
    （3）内部类的使用：在类的内部定义类
           内部类中的方法可以使用两种方法调用：
              第一种：直接使用外部类调用内部类，生成内部类的实例，在调用内部类的方法

object_name = outclass_name.inclass_name()
object_name.method()
              第二种：先对外部类进行实例化，然后再实例化内部类，最后调用内部类的方法

out_name = outclass_name()
in_name = out_name.inclass_name()
in_name.method()
     (4)__init__方法：构造函数用于初始化类的内部状态，为类的属性设置默认值（是可选的）。如果不提供__init__方法，python将会给出一个默认的__init__方法

class Fruit:
    def __init__(self, color):
        self.__color = color
        print( self.__color)
    def getColor(self):
        print( self.__color)
    def setColor(self, color):
        self.__color = color
        print(self.__color)
if __name__ == '__main__':
    color = 'red'
    fruit = Fruit(color)     #red
    fruit.getColor()         #red
    fruit.setColor('blue')   #blue
　　（5）__del__方法：构析函数用来释放对象占用的资源（是可选的）。如果程序中不提供构析函数，python会在后台提供默认的构析函数；
所以只有在需要的时候才会定义构析函数


'''