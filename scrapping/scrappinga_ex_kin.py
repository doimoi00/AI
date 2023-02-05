import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')
    titles = ul.select('li > dl > dt > a')
    for title in titles:
        print(title.get_text()) # 현재 태그를 포함하여 모든 하위 태그를 제거하고 유니코드 텍스트만 들어있는 문자열을 반환합니다. string 은 태그(tag) 내 자식 태그가 둘 이상이면, 무엇을 반환해야 하는지 명확하지 않기 때문에 None을 반환합니다
        
else : 
    print(response.status_code)