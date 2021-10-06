while True:
    s =  input("请输入判断的字符")
    if s == "q":
        print("欢迎下次使用")
        break
    if s[0].isalpha() or s[0] == '_':
        for i in s[1:]:
            if not (i.isalnum() or i == '_'):
                print("%s 变量不合法" % s)
                break
        else:
            print("%s 变量合法" %s)
    else:
            print("%s 变量不合法" % s)