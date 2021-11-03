
#부모클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식클래스 정의
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name #subject와 Student ID 안나옴 (주석처리 하면 나옴)
        # self.phoneNumber = phoneNumber #subject와 Student ID 안나옴 (주석처리 하면 나옴)
        
        Person.__init__(self,name,phoneNumber) #부모 클래스 껄 그대로 가져다 씀
        
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, student ID: {1})".format(
            self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
print(p.__dict__)
s.printInfo() 
print(s.__dict__)


print(issubclass(Student,Person))
print(issubclass(Person,Student))
print(issubclass(Student,object))
print(issubclass(Person,object))


