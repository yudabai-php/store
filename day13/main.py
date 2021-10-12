#生成测试报告
from  HTMLTestRunner import HTMLTestRunner
import unittest

#1、加载测试用例
tests =unittest.defaultTestLoader.discover(r"D:\Python\Pythondaim\day13",pattern="Test*.py")

#2、创建运行器

runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="计算器所有算法测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="w+",encoding="utf-8")
)

#3、运行用例
runner.run(tests)


# 4.邮件发送
# 代码的方式发送邮件，报告当成附件发送给我。
# 温馨提示：授权码，不是登陆密码。开启授权码。















