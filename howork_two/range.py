# range(x,y,z)函数 -----生成序列数 序列数范围为x~y-1  z代表间隔
'''
for x in range(0,10):
    print(x)
'''

'''
for x in range(0, 10, 2):   #在0~10之间生成序列数，且每隔2个数生成
    print(x,end='|')
'''

# for x in range(10, 0, -2):
#     print(x,end='|')

# 切片
a = [1, 2, 3, 4, 5, 6, 7, 8]
for x in a[0:len(a):2]:
    print(x, end=' | ')

