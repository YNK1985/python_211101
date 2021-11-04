#file_test.py

#파일에 쓰기
f=open("c:\\work\\demo.txt","wt")
f.write("첫번째\n두번째\n세번째")
f.close()

f=open("c:\\work\\demo.cvs","wt")
f.write("첫번째\n두번째\n세번째")
#메모리버퍼를 비우고 작업을 종료
f.close()

f=open("c:\\work\\demo.txt","rt")
print(f.readline())
print(f.readline())
print("하나의문자열로 읽기")
print(f.tell())
f.seek(0) #RESET임
result = f.read()
print(result)

print("리스트로 받기")
f.seek(0)
lst=f.readlines()
print(lst)

if f.closed:
    print("Closed")
else:
    f.close()


print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000))