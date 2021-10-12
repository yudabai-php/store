from unittest import TestCase
from Calc import Calc

class TestCalc(TestCase):

    def testadd1(self):
        #准备数据
        a = 5
        b = 6
        s = 11
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)

    def testadd2(self):
        #准备数据
        a = -5
        b = -6
        s = 11
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)

    def testadd3(self):
        #准备数据
        a = -5
        b = 6
        s = 1
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)

    def testadd4(self):
        #准备数据
        a = 5
        b = -6
        s = -1
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)

    def testadd5(self):
        #准备数据
        a = 500000000000000000000000000000000000000000000000000000000000
        b = 6
        s = 500000000000000000000000000000000000000000000000000000000006
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)
    def testadd6(self):
        #准备数据
        a = 5
        b = 6000000000000000000000000000000000000000000000000000000000000000
        s = 6000000000000000000000000000000000000000000000000000000000000005
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)

    def testadd7(self):
        #准备数据
        a = 0
        b = -6
        s = -6
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)

    def testadd8(self):
        #准备数据
        a = 0
        b = 6
        s = 6
        calc = Calc()
        sum = calc.add(a,b)
        #断言
        self.assertEqual(s,sum)

    def testjian1(self):
        a = 6
        b = 3
        s = 3
        calc = Calc()
        sum = calc.jian(a,b)

        self.assertEqual(s,sum)

    def testjian2(self):
        a = 3
        b = 6
        s = -3
        calc = Calc()
        sum = calc.jian(a, b)

        self.assertEqual(s, sum)

    def testjian3(self):
        a = -6
        b = -3
        s = -3
        calc = Calc()
        sum = calc.jian(a, b)

        self.assertEqual(s, sum)

    def testjian4(self):
        a = 6
        b = -3
        s = 9
        calc = Calc()
        sum = calc.jian(a, b)

        self.assertEqual(s, sum)

    def testjian5(self):
        a = -3
        b = 6
        s = -9
        calc = Calc()
        sum = calc.jian(a, b)

        self.assertEqual(s, sum)

    def testjian6(self):
        a = 600000000000000000000000000000000000000000000000000000000000000000000
        b = 3
        s = 599999999999999999999999999999999999999999999999999999999999999999997
        calc = Calc()
        sum = calc.jian(a, b)

        self.assertEqual(s, sum)

    def testjian7(self):
        a = 0
        b = 3
        s = -3
        calc = Calc()
        sum = calc.jian(a, b)

        self.assertEqual(s, sum)

    def testjian8(self):
        a = 6
        b = 0
        s = 6
        calc = Calc()
        sum = calc.jian(a, b)

        self.assertEqual(s, sum)

    def testcheng1(self):
        a = 1
        b = 2
        s = 2
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testcheng2(self):
        a = -1
        b = -2
        s = 2
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testcheng3(self):
        a = -1
        b = 2
        s = -2
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testcheng4(self):
        a = 1
        b = -2
        s = -2
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testcheng5(self):
        a = 100
        b = 10
        s = 1000
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testcheng6(self):
        a = -100
        b = 10
        s = -1000
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testcheng7(self):
        a = 100
        b = -10
        s = -1000
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testcheng8(self):
        a = 100
        b = 2
        s = 199
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testchu1(self):
        a = 1
        b = 2
        s = 0.5
        calc = Calc()
        sum = calc.cheng(a, b)

        self.assertEqual(s, sum)

    def testchu2(self):
        a = 2
        b = 1
        s = 2
        calc = Calc()
        sum = calc.chu(a, b)

        self.assertEqual(s, sum)

    def testchu3(self):
        a = -10
        b = 2
        s = -5
        calc = Calc()
        sum = calc.chu(a, b)

        self.assertEqual(s, sum)

    def testchu4(self):
        a = -10
        b = -2
        s = 5
        calc = Calc()
        sum = calc.chu(a, b)

        self.assertEqual(s, sum)



















