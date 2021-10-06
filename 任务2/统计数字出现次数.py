List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
def count (List,x):
    return List.count(x)
x = int(input("请输入需要判断出现的数："))
print("该数字在此列表中出现了：",count(List,x),"次")