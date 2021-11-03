#Function_test3.py

#기본값이 있는 경우

from typing import Protocol


def times(a=10,b=20):
    return (a*b)

#호출
print(times())
print(times(5))
print(times(4,6))
print(times(b=8))


#키워드 인자방식
def connectURI(server,port):
    strURL = "http://"+server+":"+port
    return strURL

#Call
print(connectURI("credu.com","80"))
print(connectURI(port="credu.com", server="80"))

#가변인자(수가 정해지지 않은 경우)
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","SPAM","EGG"))
print(union("a","b","c","abcd"))

#정의되지 않은 인자: 필수와 옵션이 있는 경우

def userURIBuilder(server,port,**user):
    strURL = "http://"+server+":"+port+"/?"
    for key in user.keys():
        #dict 활용
        strURL += key + "=" + user[key] + "&"
    return strURL

print(userURIBuilder("credu.com","80",id="kim", pw="1234"))
print(userURIBuilder("credu.com","80",id="kim", pw="1234",name="mike",age="30"))


#lambda:이름이 없는 간결한 함수정의 문법
g=lambda x,y:x*y
print(g(3,4))
print(g(4,5))

print((lambda x:x**x)(3))
print(globals())

