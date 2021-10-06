def parseTrigon(a, b, c):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = int(a)
    b = int(b)
    c = int(c)
    if a in arr and b in arr and c in arr:
        if a == b and b == c:
            return 3
        elif a == b and a + b > c or b == c and b + c > a or a == c and a + c > b:
            return 2
        elif  a+b >c and b+c >a and a+c>b:
            return 1
        elif a + b <= c or a + c <= b or b + c <= a:
            return 0
        else:
            return -1
a = int(input("三角形的边长：a= "))
b = int(input("三角形的边长：b= "))
c = int(input("三角形的边长：c= "))
par =  parseTrigon(a, b, c)
if par == 3:
    print("等边三角形")
if par == 2:
    print("等腰三角形")
if par == 1:
    print("普通三角形")
if par == 0:
    print("不是三角形")
if par == -1:
    print("输入非法")