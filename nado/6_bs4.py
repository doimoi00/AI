# 네이버 웹툰 스크랩핑 하기

from urllib import response
import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/index"
res= requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") # lxml 파서를 설치했고 이를 통해 파싱해 주겠다는 뜻이다. 가지고 온 html 문서를 lxml 이 파싱을 해서 BeautifulSoup 객체로 만들었고 모든 정보를 soup이 가지고 있다
# print(soup.title.get_text()) # tiltle에서 html 태그는 빼고 보여 준다
# print(soup.a) # 첫번째 a 태그를 보여 준다
# print(soup.a.attrs)   # 첫번쨰 a 태그를 dictionary 형태로 보여준다
# print(soup.a["href"]) # 첫번쨰 a 태그에서 원하는 값(여기서는 href)을 찍어주면 그것에 해당하는 값을 알려 준다
# print(soup.find("a",attrs={"class":"Nbtn_upload"})) # '웹툰 올리기'를 클릭해서 검사를 해 보니 a 태그에 class가 Nbtn_upload여서 복사해서 넣었다
# print(soup.find(attrs={"class":"Nbtn_upload"})) # a 태크 없이 그냥 class가 Nbtn_upload 인거 찾아 줘 라고 할수도 있다. 내가 보긴 이것을 가장 많이 사용할거 같다 
# print(soup.find("li",attrs={"class":"rank01"})) # '웹툰 올리기'를 클릭해서 검사를 해 보니 li 태그에 class가 rank01여서 복사해서 넣었다
# print(soup.title) # soup 객체가 가지고 있는 text에서 title만 출력해 준다

rank1= soup.find("li", attrs={"class":"rank01"})
print(rank1.a) # 첫번째 a 태그를 보여 준다
print(rank1.a.get_text()) # 첫번째 a 태그의 글만 뽑아서 보여준다

rank2=(rank1.next_sibling.next_sibling) # 다음 태그를 보여준다. 한번만  해 줘도 되는데 한번만 하면 개행 정보가 있어서 아무것도 안 나와서 next_sibling을 두번해 준 것이다
print(rank2.a.get_text())

rank3=rank2.previous_sibling.previous_sibling # 이전 태그를 보여 준다
print(rank3.a.get_text())

print("-------------------------")

print(rank1.find_next_siblings("li")) # li로 된 것을 모두 가지고 온다




