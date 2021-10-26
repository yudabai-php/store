'''

        此类判断数据的正确性

'''

class InitData:
    Login_success_data = [
        {"username":"av","name":"蔚超慧","password":"123456","pasword":"123456","age":23,
         "sex":"男","office":"测试开发","youxiang":"1031234156@qq.com","phone":"15885236547","address":"内蒙古","expect":"注册成功，请返回登录！"},
        {"username": "ad", "name": "蔚大白", "password": "123456", "pasword": "123456", "age": 24,
         "sex": "男", "office": "Python自动化", "youxiang": "104442646@qq.com", "phone": "15898746688", "address": "内蒙古乌兰察布市","expect":"注册成功，请返回登录！"},

    ]

    Login_error_data = [
        {"username": "av", "name": "蔚超慧", "password": "123456", "pasword": "123456", "age": 23,
         "sex": "男", "office": "测试开发", "youxiang": "1032256156@qq.com", "phone": "15846342389", "address": "内蒙古","expect":"该登录名已被人使用！"},
        {"username": "ad", "name": "蔚大白", "password": "123456", "pasword": "123456", "age": 24,
         "sex": "男", "office": "Python自动化", "youxiang": "106123646@qq.com", "phone": "15813256498",
         "address": "内蒙古乌兰察布市","expect":"该登录名已被人使用！"},
    ]





