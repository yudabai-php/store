'''
 猜数字游戏：
        需求：
            1.系统产生一个随机数，
            2.用户从键盘输入数据，与随机数进行比对
                2.1 若大了，温馨提示：大了
                2.2 若小了，提示：小了
                2.3 提示：恭喜您，猜中！
        技术选型：
            1.随机数技术
                import random
                random.randint(开始数据，结束数据)
            2.键盘输入技术
                name = input()
            3.判断技术：多分支判断
                if....else
                if...elif.....elif....else
            4.循环技术
                while 条件：
    任务：
        加上金币赌博功能。
            初始化有5000金币，每猜错一次，扣500金币。
            5机会，钱扣完为止。
            在机会过程中，若猜中，奖励1000金币。
            然后询问，是否继续？是，否。
            import random

'''

import random
# 1. 让系统产生一个随机数字
data = random.randint(0,200)
coin = 0
sum = 0
star = input("是否开始游戏")
if star == "1":
    coin = int(input("余额不足，请输入充值资金:"))
    if coin < 2000:
        sum = coin + (coin * 0.1)
        print("充值成功，您的余额为:", sum)
    else:
        coin > 2000
        sum =coin + (coin * 0.2)
        print("充值成功，您的余额为:", sum)
# 2.开始只猜5次  ， 范围（0~200）
i = 0
while coin >= 500 and i < 5:
    num = input("请输入您要猜的数字：")
    num = int(num)
    if num > data:
        sum = sum - 500
        i = i + 1
        print("大了！当前的金币数为:",sum,"当前剩余次数为：",5-i)
    elif num < data:
        sum = sum - 500
        i = i + 1
        print("小了！当前的金币数为：",sum,"当前剩余次数为：",5-i)
    else:
        sum = sum + 1000
        print("恭喜您，猜中数字，本次幸运数字为：",num,"你共使用了：",i,"次","当前的金币数为:",sum)
        break # 跳出循环
else:
    star == "q"


