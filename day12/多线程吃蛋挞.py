'''
    1、需求
        3个厨师   6个顾客
        有一个篮子可以放500个蛋挞
        三个厨师一起做蛋挞，判断篮子满了的话 停3s

        每个蛋挞  2元

        6个顾客同时抢蛋挞
        每人有3000块钱
        如果篮子空了 停3秒  再继续抢
'''

from threading import  Thread
import  time

tart = 0
pirce = 5

class Chef(Thread):

    name = ""
    count = 0
    def run(self) -> None:
        global tart
        while True:
            if tart >= 500:
                time.sleep(0.5)
                break
            else:
                tart = tart + 1
                time.sleep(0.5)
                print(self.name,"正在做蛋挞，现在篮子里有：",tart,"个蛋挞")

class customer(Thread):
    money = 100
    count = 0
    name = ""

    def setname(self,name):
        self.name = name

    def run(self) -> None:
        global tart
        global pirce
        while True:
            if tart < 1:
                time.sleep(0.5)
            elif tart >= 1 and self.money >= pirce:
                tart = tart - 1
                self.money = self.money - pirce
                self.count = self.count + 1
                print(self.name,"抢到了一个蛋挞，当前的余额为：",self.money)
            elif self.money < pirce:
                print(self.name,"余额不足,一共抢了",self.count,"个蛋挞！")
                break

C1 = Chef()
C1.name = "1号厨师"
C2 = Chef()
C2.name = "2号厨师"
C3 = Chef()
C3.name = "3号厨师"


c1 = customer()
c1.setname("一号顾客")
c2 = customer()
c2.setname( "二号顾客")
c3 = customer()
c3.setname("三号顾客")
c4 = customer()
c4.setname("四号顾客")
c5 = customer()
c5.setname = "五号顾客"
c6 = customer()
c6.setname = "六号顾客"


C1.start()
C2.start()
C3.start()

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()



























