'''

1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重个写所有父类的方法，每方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；


'''

class Chef:
    __username = ""
    __age = 0

    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return  self.__age

    def rice(self,cook):
        print("这名叫做：",self.__username,"的厨师，今年已经：",self.__age,"岁了，但是他的",cook,"还是做的那么好！")

class cook(Chef):


    def rice(self,cook):
        super().rice(cook)


c = cook()
c.setUsername("蔚大白")
c.setAge("69")
c.rice("开水白菜")







