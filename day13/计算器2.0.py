class calculator:
    a = 0
    b = 0

    def add(self):
        a = int(input("请输入第一个数字："))
        b = int(input("请输入第二个数字："))
        result =   a + b
        print("两数之和为{}".format(result))

    def jian(self):
        a = int(input("请输入第一个数字："))
        b = int(input("请输入第二个数字："))
        result = a - b
        print("两数之差为{}".format(result))

    def cheng(self):
        a = int(input("请输入第一个数字："))
        b = int(input("请输入第二个数字："))
        result = a * b
        print("两数之积{}".format(result))

    def chu(self):
        a = int(input("请输入第一个数字："))
        b = int(input("请输入第二个数字："))
        result = a / b
        print("两数之商{}".format(result))

a = calculator()
def dayin():
    while True:
        select = int(input("请选择您要选择的运算：1、加法 2、减法 3、乘法 4、除法,请输入您的选择："))
        if select == 1:
            a.add()
        elif select == 2:
            a.jian()
        elif select == 3:
            a.cheng()
        elif select == 4:
            a.chu()
        else:
            print("您输入的有误，请重新输入")
            continue
        choice = input('是否继续？继续输入Y，输入任意键退出。')
        if choice != 'Y':
            break

dayin()


