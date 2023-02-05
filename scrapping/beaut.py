from bs4 import BeautifulSoup

# 태그 선택자
#'h1'
#'html'
#
## 아이디 선택자 
#'#<아이디 이름>'

## 클래스 선택자
#'.<클래스 이름>.<클래스 이름>'
#
## 후손선택자
#'meigen li'
#
## 자식 선택자
#'ul.itmes > li'




html="""
<html><body>
<div id="meigen">
    <h1> 위키북스 도서 </h1>
    <ul class='items'>
        <li> 유니티 게임 이펙트 입문</li>
        <li>스위프트로 시작하는 아이폰 앱 개발 교과서 </li>
        <li>모던 웹사이트 디자인 정석</li>
        
    </ul>
<div>
</body></html>
"""

soup=BeautifulSoup(html,'html,parser')
header = soup.select_one('body > div > hi') # 한개를 선택하려고 할 경우
list_name=soup.select('ul.itmes.li') # 요소의 배열

header.string # 글자를 추출할때 사용


print(soup.select_one('ul').attrs) # 내부에 있는 요소를 선택할 때 사용
