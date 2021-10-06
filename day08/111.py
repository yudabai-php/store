import random
from mysal import update
from mysal import select

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank = {}
# bank={'Frank': {'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'ran': 38340677, 'money': 0}}
# {'Frank': {'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'ran': 38340677, 'money': 0}}
bank_name = "汉科软地球中国老牛湾分行"  # 全局变量


def bank_adduser(username, password, country, province, street, door, account, money):
    sal = "select count(*) from user"
    param = []
    date = select(sal, param, mode="one")[0]
    # print(date)
    if date > 100:
        return 3
    sal1 = 'select * from user where account=%s'
    param1 = [account]
    date1 = select(sal1, param1)
    if len(date1) > 0:
        return 2
    sal2 = 'insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    param2 = [account, username, password, country, province, street, door, money, bank_name]
    update(sal2, param2)
    return 1


def useradd():
    username = input("请输入您的用户名：")  # 局部变量
    password = input("请输入密码：")  # print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account = random.randint(10000000, 99999999)
    money = 0
    bankadd = bank_adduser(username, password, country, province, street, door, account, money)
    if bankadd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        sal = 'select money from user where account=%s'
        param = [account]
        date = select(sal, param, mode='one')[0]
        print(date)
        print(info % (username, account, country, province, street, door, date, bank_name))
    elif bankadd == 2:
        print("用户已存在")
    elif bankadd == 3:
        print("数据库已满")


def withdraw():
    account = int(input("请输入你的账号："))
    sal = "select * from user where account=%s"
    param = [account]
    date = select(sal, param)
    if len(date) > 0:
        while True:
            password = input("请输入您的密码")
            sal1 = 'select password from user where account=%s'
            param1 = [account]
            date1 = select(sal1, param1, mode='one')[0]
            if password == date1:
                withdraw_money = int(input("请输入你要取款的金额："))
                sal2 = 'select money from user where account=%s'
                param2 = [account]
                date2 = select(sal2, param2, mode='one')[0]
                if withdraw_money > date2:
                    print("您的余额不足！余额：", date2)
                    break
                else:
                    sal3 = 'update user set money =money-%s'
                    param3 = [withdraw_money]
                    date3 = update(sal3, param3)
                    print("取钱成功！您的余额为：", date3)
                    break
            else:
                n = 4
                m = 0
                print("密码不正确!您还有", n - 1, "次机会")
                m += 1
                n -= 1
                if m == 4:
                    print("该账号今日已锁定，请明天再来。")
                    break
    else:
        print("您输入的账号不存在！")


def saving():
    account = int(input("请输入你的账号："))
    sal = "select * from user where account=%s"
    param = [account]
    date = select(sal, param)
    if len(date) > 0:
        money = int(input("请输入你要存入的金额："))
        sal1 = 'update user set money=money+%s'
        param1 = [money]
        update(sal1, param1)
        sal2 = 'select money from user where account=%s'
        param2 = [account]
        date1 = select(sal2, param2)
        print("存款成功！你的余额为：", date1)
    else:
        print("您输入的账号不存在！")


def transfer():
    account = int(input("请输入您的账号"))
    sal = "select * from user where account=%s"
    param = [account]
    date = select(sal, param)
    if len(date) > 0:
        account2 = int(input("请输入您要转账的账号："))
        sal1 = "select * from user where account=%s"
        param1 = [account2]
        date1 = select(sal1, param1)
        if len(date1) > 0:
            password = input("请输入您的密码")
            sal2 = 'select password from user where account=%s'
            param2 = [account]
            date2 = select(sal2, param2, mode='one')[0]
            while True:
                if password == date2:
                    money = int(input("请输入您要转账的金额："))
                    sal3 = 'select money from user where account=%s'
                    param3 = [account]
                    date3 = select(sal3, param3, mode='one')[0]
                    if money > date3:
                        print('您的余额不足，转账失败！')
                        break
                    else:
                        sal4 = 'update user set money=money-%s'
                        param4 = [money]
                        update(sal4, param4)
                        sal5 = 'select money from user where account=%s'
                        param5 = [account]
                        date4 = select(sal5, param5)
                        print("转账成功！您的余额为：", date4)
                        break
                else:
                    n = 4
                    m = 0
                    print("密码错误！您还有", n - 1, "次机会")
                    n -= 1
                    m += 1
                    if m == 4:
                        print("您的账号今天不能继续登录！")
                        break
        else:
            print("您输入的账号不存在")
    else:
        print("您输入的账号不正确！")


def inquire():
    account = int(input("请输入您要查询的账号："))
    sal = "select * from user where account=%s"
    param = [account]
    date = select(sal, param)
    if len(date) > 0:
        password = input("请输入密码")
        sal2 = 'select password from user where account=%s'
        param2 = [account]
        date2 = select(sal2, param2, mode='one')[0]
        while True:
            if password == date2:
                sal3 = 'select * from user where account=%s'
                param3 = [account]
                date3 = select(sal3, param3)
                print(date3)
                break
            else:
                n = 4
                m = 0
                print("密码错误，您还有", n - 1, "次机会！")
                n -= 1
                m += 1
                if m == 4:
                    print("您的账号以冻结，请明天再来！")
                    break
    else:
        print("该用户不存在")


while True:  # 永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        withdraw()
    elif begin == "3":
        saving()
    elif begin == "4":
        transfer()
    elif begin == "5":
        inquire()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break
