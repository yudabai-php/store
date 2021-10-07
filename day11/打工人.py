'''
	人：年龄，性别，姓名。

	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。

	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

'''

class Person:
    __username = ""
    __sex = ""
    __age = 0

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
            print("输入非法")
        else:
            self.__age = int(age)



    def work(self,work):
        print(self.__username,"正在努力的~",work)


class Worker(Person):

    def work(self,work):

        super().work(work)


class student(Person):

    grade = ""

    def work(self,work):
        print("学号为：", self.grade, "的")
        super().work(work)



c1 = Worker()
c1.setUsername("打工人1号")
c1.setAge(45)
c1.setSex("男的")
c1.work("搬砖")


c2 = student()
c2.grade = "123456"
c2.setUsername("读书人")
c2.setAge(14)
c2.setSex("女")
c2.work("学习课本")













