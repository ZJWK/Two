# 完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数
# 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
# 如果一个数恰好等于它的因子之和，则称该数为“完全数”。
# 第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。 


import os


def Is_PerfNum(x):  # 判断x是否是完美数
    L = []  # 创建列表存储因子
    for n in range(1, x):  # 找出一个数的所有因子
        if x % n == 0:
            L.append(n)
    if sum(L) == x:  # 列表求和判断完美数
        print('%s is perfect number.' % x)
        return True
    else:
        return False


def flag():  # 判断是否继续
    print('Continue? (Y/N)')
    YN = str.upper(str(input()))  # 把输入的字符先转化为string，然后再全变为大写
    if YN == 'Y':
        return True
    elif YN == 'N':
        print('Exiting program!')
        os.system("pause")
        return False
    else:
        print("Error, wrong character!")
        return False


if __name__ == '__main__':

    i = 1
    while (flag()):
        while (not Is_PerfNum(i)):
            i = i + 1  # 不是完美数时，i + 1 测试下一位数
        i = i + 1  # 是完美数时，跳出内循环并 i + 1，为下一次进入循环做准备
