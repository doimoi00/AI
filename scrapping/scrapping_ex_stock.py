# 실행 후 file_test.txt에 저장한다

from urllib import response
import urllib.request
from bs4 import BeautifulSoup

url ='https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'

response = urllib.request.urlopen(url)

soup = BeautifulSoup(response,'html.parser')

# soup.select_one() # 찾은 것 중 가장 첫번째 html을 가지고 온다
results=soup.select('.content a')

# print('원달러:', results[0].string)
# print('원엔 환율', results[1].string)
# print('원유러 환율', results[2].string)

for result in results:
    
    if result.string:
        file = open('file_test.txt' ,'a') 
        file.write(result.string)
        file.write('\n')
        file.close()
        


