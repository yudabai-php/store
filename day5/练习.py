import copy

List1 = ["zhangsan","lisi",["zhangmazi","wangdasha"],"hello"]
List2 = [5,68,6,666,9]
List3 = copy.deepcopy(List1)
List1 [2][0] = "zhangsan"
print(List1)
print(List3)



















# list.append(10)
# print(list)
# list.remove(2) # 移除元素
# print(list)
# list.pop(4) #删除指定元素
# print(list)
# list.clear() #清空列表元素
# print(list)
# del  list
# print(list)
# list.index('zhangsan')
# print(list)
# count = list.count(1)
# print(count)

# list.sort()
# print(list)