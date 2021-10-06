import  random
print("==============================================")
print("|------------华夏人民银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")

# 银行字典
bank={}   #相当于一个空的数据库
bank_name="华夏全球银行"#全局变量
# 银行开户逻辑
'''
jason:{

    account:85563196
},
张三:{
}
'''
def bank_adduser(username,account,password,country,province,street,door,money):
    if username in bank :#如果一个变量在容器内就运行代码
        return 2
    if len(bank)>=100:
        return 3
    bank[username]={
        "username":username,
        "account": account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1
# 银行开户操作逻辑
def useradd():
    username=input("请输入您的用户名：")#局部变量
    password = input("请输入密码：")#print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    bankadd=bank_adduser(username,account,password,country,province,street,door,money)
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
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif bankadd ==2:
        print("用户已存在，请勿重复添加！")
    elif bankadd == 3:
        print("数据库已满")
# 存钱逻辑
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

#取钱
def bank_outputMoney(accout_get,password_get,output_money):
    if accout_get not in bank:
        return 1
    elif password_get != bank[accout_get]["password"]:
        return 2
    elif output_money > bank[accout_get]["money"]:
        return 3
    else:
        bank[accout_get]["money"] = bank[accout_get]["money"]  -  output_money
        return 0

#取钱逻辑
def outputMoney():
    accout_get  = input("请输入您的账号")
    password_get = input("请输入您的密码")
    output_money = int(input("请输入您取钱的金额"))
    withdrawals = bank_outputMoney(accout_get,password_get,output_money)
    if withdrawals == 1:
        print("该用户不存在")
    elif withdrawals == 2:
        print("密码不正确")
    elif withdrawals == 3:
        print("账户余额不足")
    else:
        print("取款成功，当前账户余额为：",bank[accout_get]["money"])
# 转账
def bank_transfer(out_account,in_account,outpassword_accoout,out_money):
    if out_account not in bank  or  in_account not in bank :
        return 1
    elif outpassword_accoout != bank[out_account]["password"]:
        return 2
    elif out_money > bank[out_account]["money"]:
        return 3
    else:
        bank[out_account]["money"] = bank[out_account]["money"] - out_money
        bank[in_account]["money"] = bank[in_account]["money"] + out_money
        return 0

def transfer():
    out_account = input("请输入您要转出的账号")
    in_account = input("请输入您要转入的账号")
    outpassword_accoout = input("请输入您要转出账户的密码")
    out_money = int(input("请输入您要转的金额："))
    Transfer  = bank_transfer(out_account,in_account,outpassword_accoout,out_money)
    if Transfer == 1:
        print("该用户不存在！")
    elif Transfer == 2:
        print("密码不正确！")
    elif Transfer == 3:
        print("余额不足!")
    else:
        print("转账成功！")
        print("转出账号金额为：",bank[out_account]["money"])
        print("转入账号金额为：",bank[in_account]["money"])

#查询
def search():
    account_src = input("请输入您要查询的账号")
    password_src = input("请输入您要查询账号的密码")
    if account_src in bank:
        if password_src != bank[account_src]["password"]:
            print("密码错误")
        else:
            print("查询成功，以下是您要查询的信息:")
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
            print(info % (bank[account_src]["username"], bank[account_src]["account"],
                          bank[account_src]["country"],bank[account_src]["province"], bank[account_src]["street"],
                          bank[account_src]["door"], bank[account_src]["money"], bank[account_src]["bank_name"]))

    else:
        print("账号不存在")

while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        # print("存钱")
        saveMoeny()
    elif begin == "3":
        # print("取钱")
        outputMoney()
    elif begin == "4":
        # print("转账")
        transfer()
    elif begin == "5":
        # print("查询")
        search()
    elif begin == "6":
        print("欢迎下次使用!")
        break
    else:
        print("你瞎输入什么东西！")
        break

