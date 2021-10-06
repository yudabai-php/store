# GDP = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
GDP = [5,5,6,7,8,9,10,15]
print(GDP)
sum = 0
for i in range(len(GDP)):
    sum = sum + GDP[i]
print("我国的GDP总和为：",sum)
# b = len(GDP)
avg = 0
for i in GDP:
    avg = avg + 1
print("我国前八省GDP平均值为：",sum/avg)