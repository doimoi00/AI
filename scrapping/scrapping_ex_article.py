import urllib.request
from bs4 import BeautifulSoup
import time

url ='https://n.news.naver.com/mnews/article/277/0005085236?sid=105'


response = urllib.request.urlopen(url)

soup = BeautifulSoup(response,'html.parser')

# soup.select_one() # 찾은 것 중 가장 첫번째 html을 가지고 온다
results=soup.select('#section_body a')

for result in results:
    # 기사를 가지고 옵니다
    
    print('제목:', result.attrs['title'])
    url_article= result.attrs['href']
    response = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(response,'html.parser')
    content=soup_article.select_one('#articleBodyContents')
    print(content.contents) # string은 tag안에 있는 문자열은 가지고 오지 않기 때문에 contents를 사용
    # 1초 휴식
    time.sleep(1)


    
