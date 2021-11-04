#RegularExpressions.py

import re

result =re.search("[0-9]*t","35th")  #찾았으면 매칭 객체 리턴
print(result)
print(result.group())

#Match vs search
#MAtch는 정확하게 일치
#search는 포함하고 있다면
print(bool(re.match("ap", "this is an apple")))
print(bool(re.search("ap", "this is an apple")))

print("연도")
print(bool(re.match("\d{4}","작년은 2020년")))
print(bool(re.search("\d{4}","작년은 2020년")))
print(bool(re.search("\d{5}","저기는 12584입니다.")))
print(re.search("\d{5}","저기는 12584입니다."))