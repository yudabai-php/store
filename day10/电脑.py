'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），
行为（打字，打游戏，看视频）
'''


class computer:
    __name = ""
    __pingmu = ""
    __money = 0
    __cpu = ""
    __neicun = ""
    __daiji = 0

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setPingmu(self,pingmu):
            self.__pingmu = pingmu
    def getPingmu(self):
        return  self.__pingmu

    def setMoney(self,money):
        if money < 0:
            print("你输入错误了！")
        else:
            self.__money = money
    def getMoney(self):
        return  self.__money

    def setCpu(self,cpu):
        self.__cpu = cpu
    def getCpu(self):
        return self.__cpu

    def setNeicun(self,neicun):
        self.__neicun = neicun
    def getNeicun(self):
        return  self.__neicun

    def setDaiji(self,daiji):
        self.__daiji = daiji
    def getDaiji(self):
        return  self.__daiji

    def  dazi(self,hour):
        print(self.__name,"用来使用打字系统已经：",hour,"小时")

    def playgame(self,hour):
        print(self.__name,"用来打游戏已经：",hour,"天！")

    def watch(self,hour):
        print(self.__name,"已经看了：",hour,"小时的视频！")

    def show(self):
        print("我的电脑品牌为：",self.__name,self.__cpu,self.__daiji)

p = computer()
p.setName("Hasee")
p.setCpu("i9-11000")
p.setDaiji(15)
p.setMoney(8000)
p.setPingmu("15.6寸")
p.setNeicun(16)

p.dazi(5)
p.playgame(3)
p.watch(30)
p.show()