# BankAccount.py

#은행의 계정을 표현한 클래스 

"""
class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        self.balance -= amount
    
    #원하는 문자열을 출력
    def __str__(self):
        return "{0}, {1}, {2}".format(self.id, 
        self.name, self.balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
print(account1)

account1.withdraw(3000)
print(account1)

account1.balance = 150000000
print(account1)
"""

class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    
    #원하는 문자열을 출력
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
print(account1)

account1.withdraw(3000)
print(account1)

#id, name, balance가 모두 숨겨졌기 때문에 수정, 삭제, 추가 이런거 불가함.
account1.__balance = 150000000
print(account1)
print(account1._BankAccount__balance)
# name mangling을 통해 백도어로 접근 가능하긴함.... 보안 취약함...
account1._BankAccount__balance = 150000000
print(account1._BankAccount__balance)
# print(account1.__balance)
