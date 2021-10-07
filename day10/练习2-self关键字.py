class student:
    __username = ""
    __age = 0

    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username

    def setAge(self,age):
        if 0 < age < 120:
            self.__age = age
            # print(age)

        # if age < 0 or age > 120:
        #     print("您输入的年龄非法")
        else:
            # self.__age  = age
           print("输入非法")
    def getAge(self):
        return self.__age

    def Showme(self):
        print("大家好，我叫",self.__username,"今年",self.__age,"岁了！")

    def compare(self,student):
        if self.__age > student.getAge():
            print("我比同学大，大",self.__age - student.getAge(),"岁！")
        elif self.__age < student.getAge():
            print("我比我同学小,小",student.getAge() - self.__age,"岁！")
        else:
            print("我俩一样大！")

s = student()
s.setUsername("蔚超慧")
s.setAge(18)

s1 = student()
s1.setUsername("蔚大白")
s1.setAge(20)

s.Showme()
s.compare(s1)


