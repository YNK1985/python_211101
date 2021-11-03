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
print("number:",Person.num_person)




