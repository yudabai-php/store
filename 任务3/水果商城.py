# # 开始买东西之前，提示是否要抽一张优惠券。
# # 若是：随机给一张，最终要进行使用优惠券的进行结算。
# # 若否：正常买东西
# import  random
# shop = [
#     ["劳力士手表", 200000],
#     ["Iphone 12X plus", 12000],
#     ["lenovo PC", 6000],
#     ["HUA WEI WATCH", 1200],
#     ["Mac PC", 15000],
#     ["辣条", 2.5],
#     ["老干妈", 13]
# ]
# mycart = []
# tickets = ["老干妈","lenovo"]
# i = 10
# j = 20
# try:
#     money = float(input("请输入您的余额："))
#     for key,value in enumerate(shop):
#         print(key,value)
#     while True:
#         ticket = input("是否要抽取一张优惠卷：Y/N ")
#         choose = input("请输入你想要购买的商品的编号：")
#         if choose.isdigit():
#             choose = int(choose)
#             if choose > 6:
#                 print("您输入的商品不存在！别瞎弄！")
#             else:
#                 if money > shop[choose][1]:
#                     mycart.append(shop[choose])
#                     if ticket == "Y" or ticket == "y":
#                         if i <= 0 and j <= 0:
#                             print("优惠券已用完")
#                             continue
#                         discount = random.choice(tickets)  # 从老干妈，联想优惠卷中抽取一张
#                         print("恭喜您抽中{0}的优惠卷".format(discount))
#                         if discount == "lenovo" and choose == 2:
#                             i -= 1
#                             money = money - shop[choose][1] * 0.1
#                         elif choose == 6:
#                             j -= 1
#                             money = money - shop[choose][1] * 0.7
#                         else:
# users = {"admin": "123456"}
# score = {"admin": 0}
# tickets = {"无券": 1, "免半券": 3, "满600减100券": 50, "满10000减1000券": 10, "免单券": 6}
#
# print("----------请先登录系统----------")
# username = input("请输入用户名：")
# password = input("请输入密码：")
# if username in users:
#     if password == users[username]:
#         k, v = tickets.popitem()
#         if v > 0:
#             if k != "无券":
#                 tickets[k] = v-1
#             print("恭喜您抽中{0}".format(k))
#         else:
#             k = "无券"
#             print("恭喜您抽中{0}".format(k))
#         money = float(input("请输入您的余额："))
#         for key, value in enumerate(shop):
#             print(key, value)
#         while True:
#             choose = input("请输入你想要购买的商品的编号：")
#             if choose.isdigit():
#                 choose = int(choose)
#                 if choose > 6:
#                     print("您输入的商品不存在！别瞎弄！")
#                 else:
#                     if money > shop[choose][1]:
#                         mycart.append(shop[choose])
#                         score[username] += shop[choose][1]/10
#                         if k == "免半券":
#                             money -= shop[choose][1] * 0.5
#                         elif k == "满600减100券":
#                             if shop[choose][1] >= 600:
#                                 money -= shop[choose][1]-100
#                         elif k == "满10000减1000券":
#                             if shop[choose][1] >= 10000:
#                                 money -= shop[choose][1] - 1000
#                         elif k == "无券":
#                             money -= shop[choose][1]
#                         else:
#                             money = money
#                         print("恭喜，成功添加购物车！您的余额还剩￥：", money)
#                     else:
#                         money -= shop[choose][1]
#                     print("恭喜，成功添加购物车！您的余额还剩￥：", money)
#             else:
#                     print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
#     elif choose == "q" or choose == "Q":
#         print("拜拜了，您嘞！欢迎下次光临！")
#             break
#         print("以下是您的购物小条，请拿好：")
#         for key, value in enumerate(mycart):
#             print(key, value)
#         print("本次余额还剩：{0}￥".format(money))
#     except:
#         print("输入有误，请重新输入！")
#                         print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
#             elif choose == "q" or choose == "Q":
#                 print("拜拜了，您嘞！欢迎下次光临！")
#                 break
#             print("以下是您的购物小条，请拿好：")
#             for key, value in enumerate(mycart):
#                 print(key, value)
#             print("您当前积分为：{0:.2f}".format(score[username]))
#             print("本次余额还剩：{0}￥".format(money))
#              else:
#         print("密码输入错误！")
#     else:
#         print("用户不存在！请先注册！")
