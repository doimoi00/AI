# 파일명에 requests라는 단어가 들어가면 실행이 안 된다

import requests

url='http://google.com'

session=requests.session()
response = session.get(url)
response.raise_for_status()

print(response.text)

