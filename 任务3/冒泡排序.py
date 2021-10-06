a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
print("冒泡排序前的结果：",a)
for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] =a[j+1],a[j]
print("冒泡排序后的结果：",a)