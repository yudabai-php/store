
class Air:
    __brand = ''
    __price = 0
    __time = 0

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setPrice(self, price):
        if price <= 0:
            print('价格不能为零为负！')
        else:
            self.__price = int(price)

    def getPrice(self):
        return self.__price

    def setTime(self, time):
        if time < 0:
            print('时间不能为负！！')
        else:
            self.__time = int(time)

    def power_on(self):
        print('空调开机了...')

    def shut_down(self):
        print('空调将在', self.__time, '分钟后自动关闭...')

    def show(self):
        print('空调品牌是', self.__brand, '空调价格为', self.__price, '元！')


p = Air()
p.power_on()
p.setBrand(input('输入空调品牌：'))
p.setPrice(int(input('输入空调价格：')))
p.show()
p.setTime(int(input('空调在多少分钟后关机：')))
p.shut_down()
