#Web1.py

from bs4 import BeautifulSoup

#페이지를 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup=BeautifulSoup(page,"html.parser")
# print(soup.prettify())

#<p> p태그("p") 전부 검색
# print(soup.find_all("p"))

# <p> tag 한개 검색
# print(soup.find("p"))

#<p class="outer-text"> 약간의 검색 조건
# print(soup.find_all("p", class_="outer-text"))


#태그는 삭제하고 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    #앞뒤에 태그를 삭제하고 컨텐츠만
    content = tag.text
    print(content.strip())




