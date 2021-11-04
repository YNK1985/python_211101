#try1.py


def divide(a,b):
    return a/b


try:

    result = divide(5,1)
    

except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")

except TypeError:
    print("숫자여야 합니다.")

else:
    print("결과:{0}".format(result))
finally:
    print("무조건 마무리로 실행")

