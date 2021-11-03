#연산자 오버라이드 
class NumBox:
	def __init__(self, num):
		self.Num = num
	def __add__(self, num):
		self.Num += num
	def __sub__(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n + 100 
print(n.Num)
n - 110 
print(n.Num)

#일반 메소드
class NumBox:
	def __init__(self, num):
		self.Num = num
	def add(self, num):
		self.Num += num
	def sub(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(100) 
print(n.Num)
n.sub(110) 
print(n.Num)

