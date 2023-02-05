import urllib.request
import urllib.parse


api = 'https://search.naver.com/search.naver'
values= {'where':'nexearch',
         'sm':'top_hty',
         'fbm':'1',
         'ie':'utf8',
         'query':'조중혁',
         }


params = urllib.parse.urlencode(values) # 인코딩한다
url= api+'?'+params
print(url)

data =urllib.request.urlopen(url).read()
print(data.decode('utf-8')) # utf-8 아니면 euc-kr 이 가장 많다 

#########################################################33

# url='https://www.google.co.kr/'
# savename='test.png'
# urllib.request.urlretrieve(url, savename)

# 다운로드

# mem =urllib.request.urlopen(url).read()
# print(mem.decode('euc-kr'))

# with open(savename, mode='wb') as f:
#     f.write(mem)
#     print('저장되었습니다')