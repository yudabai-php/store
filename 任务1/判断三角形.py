a = int(input("The length of the side a = "))
b = int(input("The length of the side b = "))
c = int(input("The length of the side c = "))
while True:
    if a == b and b == c:
        print("为等边三角形")
        break
    elif a == b or a == c  or  b == c:
        print("为等腰三角形")
        break
    elif a*a + b*b == c*c or  b*b + c*c == a*a or a*a + c*c == b*b:
        print("为直角三角形")
        break
    elif a != b and b != c and a != c:
        print("为普通三角形")
        break
else:
    print("不能构成三角形")
