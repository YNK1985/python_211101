#Funtion_test2

#정수, 실수, 복소수, 문자열, 튜플, 불린 (불변형)

# x=1.2
# print(id(x))
# x=2.3
# print(id(x))


# #가변형
# lst = [1,2,3]
# print(id(lst))

# lst.append(4)
# print(id(lst))

# diction = {"a":1,"b":2,"c":3}
# print(id(diction))

# diction = {"a":1,"b":2}
# print(id(diction))


#참조를 통해서 인자를 전달
def change(x):
    
    x1=x[:]
    x1[0]="H"
    # x[0]="H"
    print(x1, id(x1),id(x))

#함수를 호출
wordlist = ["j","A","M"]
print(id(wordlist))
change(wordlist)
print(wordlist)
print(id(wordlist))


