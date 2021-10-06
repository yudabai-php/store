import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={'Frank': {'password': '12345', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'account': 38340677, 'money': 20000},
'admin': {'password': '123', 'country': '中国', 'province': '北京', 'street': '001', 'door': '002', 'account': 98762739, 'money': 30000},
'aaa': {'password': '1234', 'country': '中国', 'province': '上海', 'street': '001', 'door': '002', 'account': 17263849, 'money': 40000}}
#{'Frank': {'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'account': 38340677, 'money': 0}}
bank_name="王者荣耀分行"#全局变量

def bank_adduser(username,password,country,province,street,door,account,money):
    if username in bank:  # 如果一个变量在容器内就运行代码
        return 2
    if len(bank)>=100:
        return 3
    bank[username]={
        "username":username,
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

def useradd():
    username=input("请输入您的用户名：") # 局部变量
    password = input("请输入密码：") # print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    bankadd=bank_adduser(username,password,country,province,street,door,account,money)
    if bankadd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：%s
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, password, country, province, street, door, bank[username]["money"], bank_name))
    elif bankadd ==2:
        print("用户已存在")
    elif bankadd == 3:
        print("数据库已满")

#存钱逻辑
def bank_savemoney(account, save_money):
    if account not in bank:
        return False
    else:
        bank[account]["money"] = bank[account]["money"] + save_money
        return True
#存钱操作逻辑
def savemoney():
    account = input("请输入您的账号：")
    save_money = int(input("请输入要存款的金额："))
    status = bank_savemoney(account, save_money)
    if status:
        print("存钱成功！当前余额为：", bank[account]["money"])
    else:
        print("用户不存在！")

#取钱逻辑
def bank_givemoney(account, password, give_money):
    if account not in bank:
        return 1
    elif password != bank[account]["password"]:
        return 2
    elif give_money > bank[account]["money"]:
        return 3
    else:
        bank[account]["money"] = bank[account]["money"] - give_money
        return 4

#取钱操作逻辑
def givemoney():
    account = input("请输入您的账号：")
    password = (input("请输入密码："))
    give_money = int(input("请输入取款金额："))
    status = bank_givemoney(account, password, give_money)
    if status == 1:
        print("用户名不存在！")
    elif status == 2:
        print("密码错误！")
    elif status == 3:
        print("余额不足！")
    else:
        print("取款成功，当前余额为：", bank[account]["money"])

#转账逻辑
def bank_trans(out_account, in_account, out_password, trans_money):
    if any([out_account not in bank, in_account not in bank]):
        return 1
    elif out_password != bank[out_account]["password"]:
        return 2
    elif trans_money >  bank[out_account]["money"]:
        return 3
    else:
        bank[out_account]["money"] = bank[out_account]["money"] - trans_money
        bank[in_account]["money"] = bank[in_account]["money"] + trans_money
        return 0

#转账操作逻辑
def transmoney():
    out_account = input("请输入转出账号：")
    in_account = input("请输入转入账号：")
    out_password = input("请输入转出账号密码")
    trans_money = int(input("请输入转出金额："))
    status = bank_trans(out_account, in_account, out_password, trans_money)
    if status == 1:
        print("用户不存在！")
    elif status == 2:
        print("密码错误！")
    elif status == 3:
        print("账户余额不足！")
    else:
        print("转账成功！")
        print("转出账户余额为：", bank[out_account]["money"])
        print("转入账户余额为：", bank[in_account]["money"])

#查询逻辑
def search():
    account = input("请输入要查询的账号：")
    password = input("请输入要查询的密码：")

    userExistFlag = False
    for key, value in bank.items():
        #key: username
        #value: item
        if account == str(value['account']):
            userExistFlag = True
            if password == value['password']:
                print("查询成功！")
                info = '''
                ------------个人信息------------
                        用户名:%s
                        账号:%s
                        密码:%s
                        国籍:%s
                        省份:%s
                        街道:%s
                        门牌号:%s
                        余额:%s
                        开户行名称:%s
                '''
                print(info % (key, bank[key]["account"],bank[key]["country"],
                            bank[key]["password"], bank[key]["province"], bank[key]["street"],
                          bank[key]["door"],bank[key]["money"],bank_name))
            else:
                print("密码错误！")
                return
    if userExistFlag == False:
        print("用户名不存在！")

while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        print("存钱")
        savemoney()
    elif begin == "3":
        print("取钱")
        givemoney()
    elif begin == "4":
        print("转账")
        transmoney()
    elif begin == "5":
        print("查询")
        search()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break