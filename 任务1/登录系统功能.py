userName = "ych"      #用户名
passWord = "123456"   #密码
count = 3
while count > 0 :
    username = input("请输入用户名")
    passwoed = input("请输入密码")
    if username == userName  and  passwoed == passWord:
        print("欢迎回来！")
        break
    else:
        count = count - 1
        print("您还有",count,"次机会")
    if count == 0:
        print("你没有机会了")

