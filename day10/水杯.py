'''

    分析一个水杯的属性和功能，使用类描述并创建对象
    高度，容积，颜色，材质
    能存放液体

'''

class Cup:
    __name = ""
    __high = 0
    __volume = 0
    __color = ""
    __texture = ""

    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def  setHigh(self,high):
        if high < 0 or high > 500:
            print("你家杯子500米高？")
        else:
            self.__high = high
    def getHigh(self):
        return self.__high

    def setVolume(self,volume):
        if volume < 0 or volume >1000:
            print("你家杯子可以放1000立方米水？")
        else:
            self.__volume = volume

    def getVolume(self):
        return  self.__volume

    def setColor(self,color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setTexture(self,texture):
        self.__texture = texture

    def getTexture(self):
        return self.__volume

    def high(self,high):
        print(self.__name,"它的高度为：",high,"厘米")

    def volume(self,volume):
        print(self.__name,"它的容积为：",volume,"立方米")

    def color(self,color):
        print(self.__name,"它的颜色为：",color)

    def texture(self,texture):
        print(self.__name,"它的材质为：",texture)

    def show(self):
        print("这是一个",self.__texture,"的杯子,它的高度为：",self.__high,"它的体积为：",self.__texture,"它的颜色为：",self.__color)

c = Cup()
c.setname("茶杯")
c.setHigh(20)
c.setVolume(0.05)
c.setColor("绿色")
c.setTexture("玻璃")

c.volume(10)
c.color("绿色")
c.texture("玻璃")
c.high(20)

