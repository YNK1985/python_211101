#class_test1.py

"""
#클래스 형식정의
class Person:
    #초기화메서드(생성자)
    def __init__(self):
        self.name="default name"
    #인스턴스 메서드
    def print(self):
        print("May name is {0}" .format(self.name))
#인스턴스 생성

p1=Person()
p2=Person()
#출력
p1.name="전우치"
p1.print()
p2.print()

"""
class Person:
    #위치를 잘 본다.
    num_person = 0 #클래스에 소속된 멤버변수 (초기화메서드(생성자))
    def __init__(self):
        self.name="default name"
        Person.num_person += 1
    #인스턴스 메서드
    def print(self):
        print("May name is", self.name)

p1=Person()
p2=Person()
p3=Person()
print("number:",Person.num_person)

#런타임(코드가 실행중)시에 변수를 추가(동적인 형식의 언어)-->파이썬에서는 런타임에 각 클래스와 인스턴스 이름공간에 멤버 변수를 추가하거나 삭제할 수 있다. 
Person.title= "new title"
print(p1.title)
print(p2.title)
print(Person.title)

# p1.age=30  이건 안됨
Person.age=30
print(p1.age)
print(p2.age)






