#DemoDict2.py


#tel={"young":4708,"namkung":4133}

#phone= tel

#print(tel)

#bool
#isRight=True
#print(type(isRight))

#논리식에서 비교 연산자를 사용
#x=5
#y=5
#print(x==y)
#print(x!=y)
#print(2>1)
#print(5/2)
#print(5//2)
#print(5%2)

#and는 ~이고, ~이면서
#or 연산자는 ~이거나
#print(True and True and True)
#print(True and True and False)
#print(True or False or False)

#파이썬의 판단 근거

#print(bool(0))
#print(bool())
#print(bool(1))
#print(bool(-2))
#print(bool(3.14))
#print(bool(""))
#print(bool("demo"))
#print(bool([1,2,3]))


#a=[1,2,3]
#b=a
#a[0]=38
#print(a)
#print(b)
#print(id(a),id(b))

#a=[2,3,4]
#b=a[:]
#a[1]=24
#print(a)
#print(b)
#print(id(a),id(b))

import copy
a=[1,2,3]
b=copy.deepcopy(a)
a[0]=38
print(a)
print(b)


