names = [

    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
# dict = {}
# for i in range(len(names)):
#     dict[names[i][0]] = names[i]     # 字典赋值，左边为key值，右边为value值
# print(dict)

dict={}
a={}
for i in range(len(names)):
    # for j in range(1,len(names[i])):
    a={
            "年龄":names[i][1],
        '性别':names[i][2],
        '编号':names[i][3],
        '公司':names[i][4],
        '薪资':names[i][5],
        '部门':names[i][6]

    }
    dict[names[i][0]]=a
print(dict)
