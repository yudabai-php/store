import random
import datetime
from icbc1 import update
from icbc1 import select
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
bank = {}  # 相当于一个空的数据库
bank_name = "华夏全球银行"  # 全局变量

# 银行开户逻辑
def bank_adduser(account, username, password, country, province, street, door, money, reagisterDate):
# 查询银行所有数据，判断数据是否有100条
    sql2 = "select count(*) from 银行"
    param2 = []
    date2 = select(sql2, param2,mode="one")[0]
    if date2 >= 100:
        return 3
# 查询用户名是否重复
    sql1="select * from 银行 where username = %s"
    param1=[username]
    date1 = select(sql1,param1)
    if len(date1)>0:
        return 2
    # sql语句,插入数据
    sql = "insert into 银行 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, username, password, country, province, street, door, money, reagisterDate, bank_name]
    update(sql, param)
    return 1

# 银行开户操作逻辑
def useradd():
    username = input("请输入您的用户名：")  # 局部变量
    password = input("请输入密码：")
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account = random.randint(10000000, 99999999)
    money = 0
    reagisterDate=datetime.datetime.now().strftime('%Y-%m-%d')
    bank_name=input("请输入你的开户行：")
    bankadd = bank_adduser(account, username, password, country, province, street, door, money, reagisterDate, bank_name)
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
                    时间：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        sql = 'select money from gh where account= %s'
        param = [account]
        data = select(sql, param, mode='one')[0]
        print(data)
        print(info % (username, account, country, province, street, door, data, reagisterDate, bank_name))
    elif bankadd == 2:
        print("用户已存在，请勿重复添加！")
    elif bankadd == 3:
        print("数据库已满")


# 存钱逻辑
def bank_saveMoney(account_save, save_money):
    # 判断账号是否存在
    sql3="select * from 银行 where account=%s"
    param3=[account_save]
    date3=select(sql3,param3)
    if len(date3)>0:
        # 账号存在，存入金额
        sql4="update 银行 set money=money+%s where account=%s"
        param4=[save_money,account_save]
        update(sql4,param4)
        return True
    else:
        return False
# 存钱操作代码
def saveMoeny():
    account_money = input("请输入您存钱的账号：")
    save_money = int(input("请输入您要存入的金额:"))
    deposit = bank_saveMoney(account_money, save_money)
    if deposit:
        # 查询更改后的金额
        sql5="select money from 银行 where account=%s"
        param5=[account_money]
        date5=select(sql5,param5)
        print("存款成功！当前余额：", date5)
    else:
        print("该用户不存在")


# 取钱
def bank_outputMoney(account_get, password_get, output_money):
    # 判断账户是否存在
    sql6="select * from 银行 where account=%s"
    param6=[account_get]
    date6=select(sql6,param6)
    # if len(date6)<0:
    #     return 1
    # 判断密码是否正确
    sql7="select password from 银行 where account=%s"
    param7=[account_get]
    date7=select(sql7,param7)
    # if len(date7)<0:
    #     return 2
    # 当前余额
    sql9="select money from 银行 where account=%s"
    param9=[account_get]
    date9=select(sql9,param9)
    # 判断当前金额是否大于取款金额
    # if date9<output_money:
    #     return 3

    if len(date6)>0:
        if len(date7)>0:
            if date9>output_money:
                return 0
        else:
            return 2
    else:
        return 1

# 取钱逻辑
def outputMoney():
    account_get = input("请输入您的账号")
    password_get = input("请输入您的密码")
    output_money = int(input("请输入您取钱的金额"))
    withdrawals = bank_outputMoney(account_get, password_get, output_money)
    if withdrawals == 1:
        print("该用户不存在")
    elif withdrawals == 2:
        print("密码不正确")
    elif withdrawals == 3:
        print("账户余额不足")
    else:
        # 取款后金额
        sql8 = "update 银行 set moeny=money-%s"
        param8 = [output_money]
        date8 = update(sql8, param8)
        print("取款成功，当前账户余额为：", date8)



# 转账
def bank_transfer(out_account, in_account, outpassword_accoout, out_money):
    # 判断转出的账号是否存在
    sqla="select * from 银行 account=%s"
    parama=[out_account]
    datea=select(sqla,parama)
    # 判断转入的账号是否存在
    sqlb="select * from 银行 account=%s"
    paramb=[in_account]
    dateb=select(sqlb,paramb)
    # 判断转出的账号密码是否正确
    slqc="select password from 银行 where account=%s"
    paramc=[out_account]
    datec=select(slqc,paramc)
    # 判断当前余额是否大于转出的金额
    # 当前余额
    sqld="select money from 银行 where account=%s"
    paramd=[out_account]
    dated=select(sqld,paramd)
    if len(datea)>0 and len(dateb)>0:
        if len(datec)>0:
            if dated>out_money:
                return False
            else:
                return 3
        else:
            return 2
    else:
        return 1


def transfer():
    out_account = input("请输入您要转出的账号")
    in_account = input("请输入您要转入的账号")
    outpassword_accoout = input("请输入您要转出账户的密码")
    out_money = int(input("请输入您要转的金额："))
    Transfer = bank_transfer(out_account, in_account, outpassword_accoout, out_money)
    if Transfer == 1:
        print("该用户不存在！")
    elif Transfer == 2:
        print("密码不正确！")
    elif Transfer == 3:
        print("余额不足!")
    else:
        # 转账后金额
        sqle="update 银行 set money=money-%s where account=%s"
        parame=[out_money,out_account]
        datee=update(sqle,parame)
        print("转账成功！")
        print("转出账号余额为：", datee)
        sqlf="select money from 银行 where account=%s"
        paramf=[in_account]
        datef=select(sqlf,paramf)
        print("转入账号余额为：", datef)


# 查询
def search(username, account, country, province, street, door, money, reagisterDate, bank_name):
    account_src = input("请输入您要查询的账号")
    password_src = input("请输入您要查询账号的密码")
    # 判断查询的账号是否存在
    sqlg="select *from 银行 where account=%s"
    paramg=[account_src]
    dateg=select(sqlg,paramg)
    # 查询账号的密码是否正确
    sqlh="select password from 银行 account=%s"
    paramh=[account_src]
    dateh=select(sqlh,paramh)
    if len(dateg)>0:
        if len(dateh)>0:
             #查询账号信息
            sqli="select * from 银行 where account=%s"
            parami=[account_src]
            datei=select(sqli,parami,mode="all")
            for i in datei:
                print(i)
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
                           时间：%s
                           开户行名称：%s
                       '''
        # 每个元素都可传入%
                print(info % (username, account, country, province, street, door, money, reagisterDate, bank_name))
        else:
            print("密码错误！")
    else:
        print("账号不存在！")



while True:  # 永远循环
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

