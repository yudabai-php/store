print("请输入数字")
a=int(input("第一个数字"))
b=int(input("第二个数字"))
c=int(input("第三个数字"))
d=int(input("第四个数字"))
e=int(input("第五个数字"))
f=int(input("第六个数字"))
g=int(input("第七个数字"))
a1=int(input("第八个数字"))
b1=int(input("第九个数字"))
c1=int(input("第十个数字"))
# if a>b:
#     print("十个数的最大值为：",a)
# elif b>c:
#     print("十个数的最大值为：",b)
# elif c>d:
#     print("十个数的最大值为：",c)
# elif d > e:
#     print("十个数的最大值为：",d)
# elif e > f :
#     print("十个数的最大值为：",e)
# elif f > g :
#     print("十个数的最大值为：",f)
# elif g > a1 :
#     print("十个数的最大值为：",g)
# elif a1 > b1 :
#     print("十个数的最大值为：",a1)
# elif b1 > c1 :
#     print("十个数的最大值为：",b1)
# else :
#     print("十个数的最大值为：",c1)
sum = a+b+c+d+e+f+g+a1+b1+c1
print("十个数的和为：",sum)
print("十个数的平均数为：",sum/10)
num = max(a,b,c,d,e,f,g,a1,b1,c1)
print("十个数的最大值为：",num)