i = 1
while i <= 9:
    j = 1
    while j <= i:
        sum = j * i
        print("%d x %d=%2d" % (j, i, sum), end=("\t"))
        j += 1
    print()
    i += 1
print("______________________________________________________________________________________________________________")
i = 9
while i >= 1 :
    j = 1
    while j <= i:
        sum = j*i
        print("%d x %d=%2d"%(j,i,sum),end=("\t"))
        j += 1
    print()
    i -= 1

print("______________________________________________________________________________________________________________")

for i in range(1,10):
    for j in range(1,i+1):
        print(j,'x',i,'=',i*j,end='\t')
    print()
