from urllib import request
from bs4 import BeautifulSoup

content = request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109')  #  코드를 가지고 온다

soup = BeautifulSoup(content, 'html.parser')




for data in soup.select('data'):
    print('시간:', data.select_one('tmef').string)
    print('시간:', data.select_one('wf').string)
    print('---------------------')


###########################################################################