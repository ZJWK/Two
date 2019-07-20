# "3位水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个"3位水仙花数"，
# 则：A的3次方＋B的3次方＋C的3次方 = ABC。


shuixianhua=[]
for i in range(1,10):
  for j in range(10):
    for k in range(10):
      if i*i*i + j*j*j + k*k*k == 100*i + 10*j + k:
        shuixianhua.append(100*i + 10*j + k)
for i in shuixianhua:
  if i == shuixianhua[-1]:
    print(i)
  else:
    print(i, end = ',')

