import random


#random.sample method 사용

lotto_num1= random.sample(range(1,46),6)
print(lotto_num1)


#while 문 사용
lotto_num2=[]

while len(lotto_num2) <6:
    a=random.randint(1,45)
    if a not in lotto_num2:
        lotto_num2.append(a)

lotto_num2.sort()

print(f'{lotto_num2}')
print(lotto_num2)