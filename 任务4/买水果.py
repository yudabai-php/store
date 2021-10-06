#买水果第一步
# info = {"水果名称":"价格"}
#
# info ['苹果'] = 32.8
# info ['香蕉'] = 22
# info ['葡萄'] = 15.5
#
# for i in info:
#     print(i,info[i])

#买水果第二步

# def returnSum(dict):
#     sum = 0
#     for i in dict:
#         sum = sum + dict[i]
#     return sum
#
# friuts = {
#     '苹果':12.3,   #水果的价格
#     '草莓':4.5,
#     '香蕉':6.3,
#     '葡萄':5.8,
#     '橘子':6.4,
#     '樱桃':15.8
# }
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money':friuts["苹果"] *4 + friuts["草莓"] *13 + friuts["香蕉"] *10
#     },
#     '小刚':{
#         'fruits':{'葡萄':19, '橘子':12, '樱桃':30},
#         'money':returnSum(friuts)
#     }
# }
# print(info)



lst = [
    ('苹果', 32.8),
    ('香蕉', 22),
    ('葡萄', 15.5)
    ]
lst_dic = dict(lst)
print('您的购物清单为')
info = '''
        '苹果': %s
        '香蕉': %s
        '葡萄': %s
        '''
print(info % (lst_dic['苹果'], lst_dic['香蕉'], lst_dic['葡萄']))


fruits = {
        '苹果': 12.3,
        '草莓': 4.5,
        '香蕉': 6.3,
        '葡萄': 5.8,
        '橘子': 6.4,
        '樱桃': 15.8
        }
fruits_mm = {'小明': {'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10}, 'money': 0}}
fruits_gg = {'小刚': {'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30}, 'money': 0}}
mm, gg = 0, 0
for i in fruits.keys():
    if i in fruits_mm['小明']['fruits']:
        mm = mm + fruits[i]*fruits_mm['小明']['fruits'][i]
    if i in fruits_gg['小刚']['fruits']:
        gg = gg + fruits[i]*fruits_gg['小刚']['fruits'][i]

info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': mm
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': gg
    }
    }
print(info)