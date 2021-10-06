'''
    python : int, float,str("" ''),bool(True,False)
    容器数据类型：
        元祖：(,234,,6,345,245,6,7,3,,26,)一旦写死，任务数据都无法修改
        列表：[2,45,6,1] 可以进行增删改查
        字典：{
            "010":"北京"
            "020":"上海"
        }
        集合：Sets:{10,20,30,46,12}
'''
'''
    教务管理系统：
        1、随机点名成名
        2、随机处罚遍数
    一、输入业务编号
        1、随机点名
        2、产生0~200范围内的处罚遍数
        q或Q，提出
    二、技术选型
        random
        判断
        循环
'''
import random
names = ["张三","李四","王五","赵六","周七","郑八","钱九","冯十"]
chenfa = ["深蹲","罚站","蛙跳","500米","叫家长","坐雅座","挨板子"]
while True: #永远循环
    chose = input("请输入选择 1：随机点名： 2：处罚遍数：")
    if chose == "1":
        # 随机产生一个角标
        index = random.randint(0,len(names)-1)
        print("恭喜",names[index],"被抓到了")
    elif chose == "2":
        xiangmu = random.randint(0,len(chenfa)-1)
        print("处罚",chenfa[xiangmu])
        print("进行",random.randint(0,150),"次")
    elif chose == "q" or chose == "Q":
        print("欢迎下次使用！")
        break
    else:
        print("输入非法！")







# print(names)