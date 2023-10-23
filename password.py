password = 'a123456'
i = 3   #储存剩余机会
while i > 0:
    pwd = input('请输入密码：')
    if pwd == password:
        print('登入成功')
        break #跳出循环
    else:
        i = i - 1
        print('密码错误，还剩', i,'机会')
        
