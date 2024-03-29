
# input()函数默认接收的是字符串
'''
一、元祖tuple：
type（（1））
因为元祖和int冲突了，在python中会把它作为int类型。
定义只有一个元素的元祖
（1，）

ord（）———转化为ascii码
eg：ord（’a’)
      97

Python中什么是set
dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。
有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。
set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：
>>> s = set(['A', 'B', 'C'])
可以查看 set 的内容：
>>> print s
set(['A', 'C', 'B'])
请注意，上述打印的形式类似 list， 但它不是 list，仔细看还可以发现，打印的顺序和原始 list 的顺序有可能是不同的，因为set内部存储的元素是无序的。
因为set不能包含重复的元素，所以，当我们传入包含重复元素的 list 会怎么样呢？
>>> s = set(['A', 'B', 'C', 'C'])
>>> print s
set(['A', 'C', 'B'])
>>> len(s)
3
结果显示，set会自动去掉重复的元素，原来的list有4个元素，但set只有3个元素。


二、Python之 访问set
由于set存储的是无序集合，所以我们没法通过索引来访问。
访问 set中的某个元素实际上就是判断一个元素是否在set中。
例如，存储了班里同学名字的set：
>>> s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
我们可以用 in 操作符判断：
Bart是该班的同学吗？
>>> 'Bart' in s
True
Bill是该班的同学吗？
>>> 'Bill' in s
False
bart是该班的同学吗？
>>> 'bart' in s
False
看来大小写很重要，'Bart' 和 'bart'被认为是两个不同的元素。


Python之 set的特点
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
最后，set存储的元素也是没有顺序的。
set的这些特点，可以应用在哪些地方呢？
星期一到星期日可以用字符串'MON', 'TUE', ... 'SUN'表示。
假设我们让用户输入星期一至星期日的某天，如何判断用户的输入是否是一个有效的星期呢？
可以用 if 语句判断，但这样做非常繁琐：
x = '???' # 用户输入的字符串if x!= 'MON' and x!= 'TUE' and x!= 'WED' ... and x!= 'SUN':
print 'input error'
else:
print 'input ok'
注意：if 语句中的...表示没有列出的其它星期名称，测试时，请输入完整。
如果事先创建好一个set，包含'MON' ~ 'SUN'：
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
再判断输入是否有效，只需要判断该字符串是否在set中：
x = '???' # 用户输入的字符串if x in weekdays:
print 'input ok'
else:
print 'input error'
这样一来，代码就简单多了。


Python之 遍历set
由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现。
直接使用 for 循环可以遍历 set 的元素：
>>> s = set(['Adam', 'Lisa', 'Bart'])
>>> for name in s:
... print name
...
Lisa
Adam
Bart
注意: 观察 for 循环在遍历set时，元素的顺序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。
Python之 更新set
由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：
一是把新的元素添加到set中，二是把已有元素从set中删除。
添加元素时，用set的add()方法：
>>> s = set([1, 2, 3])
>>> s.add(4)
>>> print s
set([1, 2, 3, 4])
如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了：
>>> s = set([1, 2, 3])
>>> s.add(3)
>>> print s
set([1, 2, 3])
删除set中的元素时，用set的remove()方法：
>>> s = set([1, 2, 3, 4])
>>> s.remove(4)
>>> print s
set([1, 2, 3])
如果删除的元素不存在set中，remove()会报错：
>>> s = set([1, 2, 3])
>>> s.remove(4)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 4
所以用add()可以直接添加，而remove()前需要判断。



三、Python之什么是dict
我们已经知道，list 和 tuple 可以用来表示顺序集合，例如，班里同学的名字：
['Adam', 'Lisa', 'Bart']
或者考试的成绩列表：
[95, 85, 59]
但是，要根据名字找到对应的成绩，用两个 list 表示就不方便。
如果把名字和分数关联起来，组成类似的查找表：
'Adam' ==> 95
'Lisa' ==> 85
'Bart' ==> 59
给定一个名字，就可以直接查到分数。
Python的 dict 就是专门干这件事的。用 dict 表示“名字”-“成绩”的查找表如下：
d = {
'Adam': 95,
'Lisa': 85,
'Bart': 59
}
我们把名字称为key，对应的成绩称为value，dict就是通过 key来查找 value。
花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。
由于dict也是集合，len() 函数可以计算任意集合的大小：
>>> len(d)
3
注意: 一个 key-value 算一个，因此，dict大小为3。


Python之访问dict
我们已经能创建一个dict，用于表示名字和成绩的对应关系：
d = {
'Adam': 95,
'Lisa': 85,
'Bart': 59
}
那么，如何根据名字来查找对应的成绩呢？
可以简单地使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict使用key：
>>> print d['Adam']
95
>>> print d['Paul']
Traceback (most recent call last):
File "index.py", line 11, in <module>
print d['Paul']
KeyError: 'Paul'
注意: 通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。
要避免 KeyError 发生，有两个办法：
一是先判断一下 key 是否存在，用 in 操作符：
if 'Paul' in d:
print d['Paul']
如果 'Paul' 不存在，if语句判断为False，自然不会执行 print d['Paul'] ，从而避免了错误。
二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：
>>> print d.get('Bart')
59
>>> print d.get('Paul')
None

Python中dict的特点
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。
由于dict是按 key 查找，所以，在一个dict中，key不能重复。
dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：
d = {
'Adam': 95,
'Lisa': 85,
'Bart': 59
}
当我们试图打印这个dict时：
>>> print d
{'Lisa': 85, 'Adam': 95, 'Bart': 59}
打印的顺序不一定是我们创建时的顺序，而且，不同的机器打印的顺序都可能不同，这说明dict内部是无序的，不能用dict存储有序的集合。
dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。
可以试试用list作为key时会报什么样的错误。
不可变这个限制仅作用于key，value是否可变无所谓：
{
'123': [1, 2, 3], # key 是 str，value是list
123: '123', # key 是 int，value 是 str
('a', 'b'): True # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
最常用的key还是字符串，因为用起来最方便。


Python更新dict
dict是可变的，也就是说，我们可以随时往dict中添加新的 key-value。比如已有dict：
d = {
'Adam': 95,
'Lisa': 85,
'Bart': 59
}
要把新同学'Paul'的成绩 72 加进去，用赋值语句：
>>> d['Paul'] = 72
再看看dict的内容：
>>> print d
{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 59}
如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value：
>>> d['Bart'] = 60
>>> print d
{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 60}


Python之 遍历dict
由于dict也是一个集合，所以，遍历dict和遍历list类似，都可以通过 for 循环实现。
直接使用for循环可以遍历 dict 的 key：
>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
>>> for key in d:
... print key
...
Lisa
Adam
Bart
由于通过 key 可以获取对应的 value，因此，在循环体内，可以获取到value的值。



四、Python创建list
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
比如，列出班里所有同学的名字，就可以用一个list表示：
>>> ['Michael', 'Bob', 'Tracy']
['Michael', 'Bob', 'Tracy']
list是数学意义上的有序集合，也就是说，list中的元素是按照顺序排列的。
构造list非常简单，按照上面的代码，直接用 [ ] 把list的所有元素都括起来，就是一个list对象。通常，我们会把list赋值给一个变量，这样，就可以通过变量来引用list：
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates # 打印classmates变量的内容
['Michael', 'Bob', 'Tracy']
由于Python是动态语言，所以list中包含的元素并不要求都必须是同一种数据类型，我们完全可以在list中包含各种数据：
>>> L = ['Michael', 100, True]
一个元素也没有的list，就是空list：
>>> empty_list = []

Python按照索引访问list
由于list是一个有序集合，所以，我们可以用一个list按分数从高到低表示出班里的3个同学：
>>> L = ['Adam', 'Lisa', 'Bart']
那我们如何从list中获取指定第 N 名的同学呢？方法是通过索引来获取list中的指定元素。
需要特别注意的是，索引从 0 开始，也就是说，第一个元素的索引是0，第二个元素的索引是1，以此类推。
因此，要打印第一名同学的名字，用 L[0]:
>>> print L[0]
Adam
要打印第二名同学的名字，用 L[1]:
>>> print L[1]
Lisa
要打印第三名同学的名字，用 L[2]:
>>> print L[2]
Bart
要打印第四名同学的名字，用 L[3]:
>>> print L[3]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range
报错了！IndexError意思就是索引超出了范围，因为上面的list只有3个元素，有效的索引是 0，1，2。
所以，使用索引时，千万注意不要越界。

Python之倒序访问list
我们还是用一个list按分数从高到低表示出班里的3个同学：
>>> L = ['Adam', 'Lisa', 'Bart']
这时，老师说，请分数最低的同学站出来。
要写代码完成这个任务，我们可以先数一数这个 list，发现它包含3个元素，因此，最后一个元素的索引是2：
>>> print L[2]
Bart
有没有更简单的方法？
有！
Bart同学是最后一名，俗称倒数第一，所以，我们可以用 -1 这个索引来表示最后一个元素：
>>> print L[-1]
Bart
Bart同学表示躺枪。
类似的，倒数第二用 -2 表示，倒数第三用 -3 表示，倒数第四用 -4 表示：
>>> print L[-2]
Lisa
>>> print L[-3]
Adam
>>> print L[-4]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range
L[-4] 报错了，因为倒数第四不存在，一共只有3个元素。
使用倒序索引时，也要注意不要越界。


Python之添加新元素
现在，班里有3名同学：
>>> L = ['Adam', 'Lisa', 'Bart']
今天，班里转来一名新同学 Paul，如何把新同学添加到现有的 list 中呢？
第一个办法是用 list 的 append() 方法，把新同学追加到 list 的末尾：
>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.append('Paul')
>>> print L
['Adam', 'Lisa', 'Bart', 'Paul']
append()总是把新的元素添加到 list 的尾部。
如果 Paul 同学表示自己总是考满分，要求添加到第一的位置，怎么办？
方法是用list的 insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素：
>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.insert(0, 'Paul')
>>> print L
['Paul', 'Adam', 'Lisa', 'Bart']
L.insert(0, 'Paul') 的意思是，'Paul'将被添加到索引为 0 的位置上（也就是第一个），而原来索引为 0 的Adam同学，以及后面的所有同学，都自动向后移动一位。


Python从list删除元素
Paul同学刚来几天又要转走了，那么我们怎么把Paul 从现有的list中删除呢？
如果Paul同学排在最后一个，我们可以用list的pop()方法删除：
>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> L.pop()
'Paul'
>>> print L
['Adam', 'Lisa', 'Bart']
pop()方法总是删掉list的最后一个元素，并且它还返回这个元素，所以我们执行 L.pop() 后，会打印出 'Paul'。
如果Paul同学不是排在最后一个怎么办？比如Paul同学排在第三：
>>> L = ['Adam', 'Lisa', 'Paul', 'Bart']
要把Paul踢出list，我们就必须先定位Paul的位置。由于Paul的索引是2，因此，用 pop(2)把Paul删掉：
>>> L.pop(2)
'Paul'
>>> print L
['Adam', 'Lisa', 'Bart']



字符串的截取
     [开始取值的数：结束取值的数]   注：不包含结束取值的数
     [开始取值的数：]                          一直取到最后一个字符
     [：结束取值的数]                          从末尾取到开头

















account = 'python'
password = '123456'
print('please input account:')
user_account = input()
print('please input password:')
user_password = input()
if account == user_account and password == user_password:
    print('success')
else:
    print('fail')

'''
