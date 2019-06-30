# 斐波那契数列（Fibonacci sequence），由数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
# 故又称为“兔子数列”。
# 形如：1、1、2、3、5、8、13、21、34、……
# 在数学上，斐波纳契数列以如下递推的方法定义：
# F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）


a=1
b=1
i=1
while i <=20 :
    print(a,end=' ')
    m=a
    a=b
    b=m+b   # 用 a,b = b,a+b 也可以实现
    i=i+1
