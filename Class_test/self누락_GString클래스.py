str = "Not Class Member" #전역변수
class GString:
    def __init__(self):
        self.str = ""  #인스턴스 멤버 변수 self.str
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str) #버그가 발생했다... -> self.str

#인스턴스 (복사본) 생성
g = GString()
g.set("First Message")
g.print()
