# 印象笔记
# https://app.yinxiang.com/shard/s20/nl/19065121/475b943c-afea-4f6d-83c6-fe9707f4ab76?title=Python%E4%B9%8B%20for%E5%BE%AA%E7%8E%AF
# input()函数默认接收的是字符串
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


