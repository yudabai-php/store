a = [1,5,21,30,15,9,30,24]

sum = 0
for i in a:
    if i % 5 == 0:
        sum = sum + i
print(sum)

# print(sum([i for i in a if i % 5 == 0])) 高级做法