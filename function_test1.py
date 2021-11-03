#function_test1.py
"""
print("함수정의")
def setValue(newValue):
    x=newValue
   
print("함수호출")
result = setValue(5)
print(result)

print("함수정의")
def setValue(newValue):
    x=newValue
    return x
print("함수호출")
result = setValue(5)
print(result)


print("함수정의")
def swap(x,y):
    return y, x
print("함수호출")
print(swap(4,7))



print("intersect 함수 정의")
def intersect(prelist, postlist):
    #지역변수에 리스트로 저장하기
    result =[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)

    return result

rstinter=intersect("HAM","SPAM")
print("함수호출", rstinter)
"""

dctA={"a":1,"b":2}

print(type(dctA))
print(id(dctA))
print(dctA)


