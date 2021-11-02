
print("구구단")
for i in [2,3,4,5,6,7,8,9]:
    print("{0}단".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0}*{1}={2}".format(i,j,i*j))


print("break")
lst=[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("item:{0}".format(item))

print("continue")
for item in lst:
    if item %2==0:
        continue
    print("item:{0}".format(item))

