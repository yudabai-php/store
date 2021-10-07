'''

猴子类：属性：类别，性别，身体颜色，体重。
行为：造火（要求传入造火的材料：比如木棍还是石头），
学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
'''

class monkey:
    __name = None
    __sort = None
    __sex = None
    __color = None
    __weight = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSort(self,sort):
        self.__sort = sort
    def getSort(self):
        return self.__sort

    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return  self.__color

    def setWeight(self,weight):
        self.__weight = weight
    def getWeight(self):
        return  self.__weight


    def fire(self,materials):
        print("这只叫",self.__name,"猴子会使用",materials,"来进行生火！")

    def studt(self,thing):
        print("这只叫",self.__name,"猴子会学习、模仿",thing,"来促进自己！")
    def show(self):
        print("这只猴子叫",self.__name,"它的体重为：",self.__weight,"kg，它的颜色为：",self.__color,"它的性别为：",self.__sex)

m = monkey()
m.setName(input("请输入猴子的名称："))
m.setSex(input("请输入猴子的性别："))
m.setColor(input("请输入猴子的颜色："))
m.setWeight(input("请输入猴子的体重："))
m.show()

m.fire(input("请输入您要使用的工具："))
m.studt(input("请输入您要学习的东西："))







