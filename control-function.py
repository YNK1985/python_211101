#제어문

list(range(10))
print()

list(range(3,8))
list(range(23,2,-1))
list(range(11,27,2))

result=list(range(2014,2022))
print(result)
day=list(range(1,32))
print(day)

print("수열함수")
for i in range(10):
    print(i)

print("list comprehensions")

lst=[1,2,3,4,5,6,7,8,9,10]
result= [i**2 for i in lst if i>5]
print(lst, result)

lst1=list(range(0,10,1))
result3=[j**2 for j in lst1 if j>5]
print(lst1, result3)


test=("apple","banana","orange")
result1=[len(i) for i in test]
print(test, result1)
