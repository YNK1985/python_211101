#Web2.py

#웹서버에 요청
import urllib.request

#웹크롤링
from bs4 import BeautifulSoup

#패키지명.파일명.함수명
# data =urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

# #검색이 용이한 객체를 생성
# soup=BeautifulSoup(data, "html.parser")
# # <td class="title">
# # 	<a href="/webtoon/detail?titleId=20853&no=49&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','49')">마음의 소리 49화 &lt;지혜&gt;</a>
# # </td>

# cartoons = soup.find_all("td", class_="title")
# print("Number:{0}".format(len(cartoons)))
# title = cartoons[0].find("a").text
# link=cartoons[0].find("a")["href"]
# print(title)
# print(link)


# #반복해서 가져오기
# for tag in cartoons:
#     title = tag.find("a").text
    
#     print (title.strip())

#수열함수로 페이지 번호를 생성
# for i in range(1,6):
#     url="https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=2" + str(i)
#     print(url)
#     data = urllib.request.urlopen(url)
#     soup=BeautifulSoup(data, "html.parser")
#     cartoons = soup.find_all("td", class_="title")

#     for tag in cartoons:
#         title = tag.find("a").text
        
#         print (title.strip())
f=open("c:\\work\\cartoon.cvs", "a")#, encoding="utf-8")
for i in range(1,6):
    url="https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=2" + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    soup=BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")

    for tag in cartoons:
        title = tag.find("a").text
        
        print (title.strip())
        f.write(title.strip()+ "\n")

f.close()

