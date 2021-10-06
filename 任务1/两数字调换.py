A = int(input("第一个数为：  "))
B = int(input("第二个数为：  "))
print("调换前顺序为：",A,B)
A = A + B
B = A - B
A = A - B
print("调换后顺序为：",A,B)