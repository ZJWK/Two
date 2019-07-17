a = [['apple', 'banana', 'origine', 'grape'], (1, 2, 3)]

for x in a:
    for y in x:
        if y == 'banana':
            break
        print(y)
        # print(y, end=' ')    # end 代表结尾不用默认的换行，而更改为以空格来结束，所以就可以打印在一行了
        # print(y)
else:
    print('no fruit')



# break 终止整个循环；continue终止当前循环
'''
b = [1, 2, 3]
for i in b:
    if i == 2:
        continue
        # break
    print(i)
'''