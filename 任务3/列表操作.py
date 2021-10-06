# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
avg = 0  # 平均薪资
avg = (names[0][5] + names[1][5] + names[2][5] + names[3][5] )/4
print("平均工资为",avg)

#平均年龄
age = 0
a = int(names[0][1])
b = int(names[1][1])
c = int(names[2][1])
d = int(names[3][1])
avg = (a+b+c+d)/4
print("平均年龄:",avg)

#向列表中插入数据
names.insert(3,["刘备","45","男","220","alibaba",500,"30"])
print(names)

# 统计
names1 = []
for i in names:
    for j in i:
        names1.append(j)
a = names1.count('男')
print("男生出现的次数：",a)
b = names1.count('女')
print("女生出现的次数：",b)

#统计每个部门的人数
count50  = names1.count("50")
print("50部门的人数为：",count50)
count60 = names1.count("60")
print("60部门的人数为：",count60)
count10 = names1.count("10")
print("10部门的人数为：",count10)