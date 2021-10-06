'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random

# 1.准备一个数据库 和 银行名称
bank = {}  # 空的数据库
'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{

        }


    }

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是狗已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if username in bank:
        return 2
    # 3.正常开户
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, gate, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))

def bank_saveMoney(account_save,save_money):
    if account_save not in bank:
        return False
    else:
        bank[account_save]["money"] = bank[account_save]["money"] + save_money
        return True
#存钱操作代码
def saveMoeny():
    account_money =  input("请输入您存钱的账号：")
    save_money = int(input("请输入您要存入的金额:"))
    deposit = bank_saveMoney(account_money,save_money)
    if deposit:
        print("存款成功！当前余额：",bank[account_money]["money"])
    else:
        print("该用户不存在")


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        saveMoeny()
        pass
    elif chose == "3":
        pass
    elif chose == "4":
        pass
    elif chose == "5":
        pass
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")








