results = [
    ["罗恩", 23, 35, 44],
    ["哈利", 60, 77, 68, 88, 90],
    ["赫敏", 97, 99, 89, 91, 95, 90],
    ["马尔福", 100, 85, 90]
]
sum = 0
for i in results:
    for j in range(1,len(i)):
        sum = sum + i[j]
    print(sum)
    sum = 0










