'''

人类：
属性:
姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。
功能：
发短信（要求参数传入短信内容）。
打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，
若为空或者小于1元则报相对应的错误信息，否则的话拨通。结束后，按照时间长度扣费并返回扣费
（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））

'''



class person:
    __username = ""
    __sex = ""
    __age = None
    __cost = 0   #剩余话费
    __brand = ""  #电话品牌
    __battery = 0 #电池容量
    __size = 0  #屏幕大小
    __standbt = 0 #最大待机时长
    __integral = 0 #积分

    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username

    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

    def setAge(self,age):
        if age < 0 or age > 130:
            print("输入非法！")
        else:
            self.__age = int(age)
    def getAge(self):
        return  self.__age

    def setCost(self,cost):
        self.__cost = float(cost)

    def getCost(self):
        return self.__cost

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setBattery(self, battery):
        if battery < 0:
            print('电池容量不能为负！')
        else:
            self.__battery = float(battery)

    def getBattery(self):
        return self.__battery

    def setSize(self, size):
        if size <= 0:
            print('屏幕大小输入非法！')
        else:
            self.__size = float(size)

    def getSize(self):
        return self.__size

    def setStandby(self, standby):
        self.__standby = int(standby)

    def getStandby(self):
        return self.__standby

    def setIntegral(self, integral):
        if integral < 0:
            print('积分不能为负！')
        else:
            self.__integral = int(integral)

    def getIntegral(self):
        return self.__integral

    def show(self):
        print('姓名', self.__username, '\n性别', self.__sex, '\n年龄', self.__age, '\n所拥有的手机剩余话费',
              self.__cost, '元！\n手机品牌', self.__brand, '\n手机电池容量', self.__battery, '%\n屏幕大小',
              self.__size, '寸\n最大待机时长', self.__standby, '分钟\n所拥有积分：', self.__integral)


p = person()
p.setUsername(input('输入姓名'))
p.setSex(input('输入性别'))
p.setAge(int(input('输入年龄')))
p.setCost(float(input('输入手机剩余话费')))
p.setBrand(input('输入手机品牌'))
p.setBattery(float(input('输入电池容量')))
p.setSize(float(input('输入手机屏幕大小')))
p.setStandby(int(input('输入手机最大待机时长')))
p.setIntegral(int(input('输入拥有积分')))
p.show()


cc = p.getCost()
dd = p.getIntegral()

while True:
    a = int(input('需要发短信还是打电话：（1或2）'))
    if a == 1:
        a_1 = input('输入短信内容：')
        print('短信内容为：\n', a_1)
        break
    elif a == 2:
        a_1 = int(input('输入电话号码：'))
        a_2 = int(input('输入打多长时间：'))
        if a_1 == None: print('不能为空！')
        elif a_1 <= 1: print('电话费不够了！')
        else:
            print('电话已拨通！')
        if a_2 >= 0 and a_2 <= 10:
            if dd >= a_2 * 15:
                dd -= a_2 * 15
            else:
                cc -= a_2 * 1
        elif a_2 > 10 and a_2 <=20:
            if dd >= a_2 * 39:
                dd -= a_2 * 39
            else:
                cc -= a_2 * 0.8
        else:
            if dd >= a_2 * 48:
                dd -= a_2 * 48
            else:
                cc -= a_2 * 0.65
        break

print('剩余话费为：', cc)
print('剩余积分为：', dd)











