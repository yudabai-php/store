from  unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from threading import  Thread
from  工商银行完整版 import  *

# class runner(Thread):
#     def run(self) -> None:
#         return
#

# username,password,country,province,street,door,money
#工商银行添加用户代码
data_addUser = [
    ["jason","123456","中国","安徽省","桃源铝","s001",6000,1],
    ["jason","123456","中国","安徽省","桃源铝","s001",6000,2],
    ["jasons1", "123456", "中国", "安徽省", "桃源铝", "s001", 6000, 1],
    ["jasons","123456","中国","安徽省","桃源铝","s001",6000,3]
]

@ddt
class TestBankUser(TestCase):

    for i in range(98):
        name = "jason" + str(i)
        bank_addUser(name,"123456","中国","安徽省","桃源铝","s001",6000)
        # print(i)


        @data(*data_addUser)  #引入数据源
        @unpack
        def testAddUser(self,a,b,c,d,e,f,g,h):
            s = bank_addUser(a,b,c,d,e,f,g)
            self.assertEqual(h,s)



#工商银行存钱测试。
data_saveMoney = [
    ["12345678",500,False],
    ["66668888",400,False],
    ["32145687",300,False],
]

@ddt
class TestBanksave(TestCase):
        @data(*data_saveMoney)
        @unpack
        def testSave(self,save_account,save_money,status):
            result = bank_saveMoney(save_account,save_money)
            self.assertEqual(result,status)

#工商银行取钱测试
data_takeMoney = [
    ["12345678",132456,500,0],
    ["21345687",123456,600,0],
    ["96374185",123456,900,0],
    ["98745685",123456,800,0]
]

@ddt
class TestBankTake(TestCase):
    @data(*data_takeMoney)
    @unpack
    def testtake(self,take_account,take_password,take_money,status):
        result = bank_takeMoney(take_account,take_password,take_money)
        self.assertEqual(result,status)

#工商银行转账测试    bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney):
data_transformMoney = [
    [12345678,85274196,123456,500,1],
    [96385274,12345698,123456,500,1],
    [78965412,63524196,456321,500,1],
    [65432189,85274166,123456,500,1],
    [96385274,12359871,123456,500,1]
]

@ddt
class TestBankTrans(TestCase):
    @data(*data_transformMoney)
    @unpack
    def testtransform(self,out_acount,in_acount,out_password,out_money,status):
        result = bank_transformMoney(out_acount,in_acount,out_password,out_money)
        self.assertEqual(result,status)


#工商银行查询功能测试
data_selectUser = [
    [12345678,123456,None],
    [23457891,321654,None],
    [15889945,415263,None]
]

@ddt
class TestBankselect(TestCase):
    @data(*data_selectUser)
    @unpack
    def testSelect(self,select_account,select_password,status):
        result = bank_selectUser(select_account,select_password)
        self.assertEqual(result,status)

# t1 = TestBankUser()
# t2 = TestBanksave()
# t3 = TestBankTake()
# t4 = TestBankTrans()
# t5 = TestBankselect()
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()






















