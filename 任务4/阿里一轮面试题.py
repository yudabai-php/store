'''
编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
'''

def count(List = []):
    for i in List:
      if i not in  list_dict:
          list_dict[i] = 1
      else:
          list_dict[i] += 1
List1 = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
list_dict ={}
count(List1)
print(list_dict)

'''
def count():
    List1 = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
    for i in List:
      if i not in  list_dict:
          list_dict[i] = 1
      else:
          list_dict[i] += 1
List1 = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
list_dict ={}
count()
print(list_dict)
'''

