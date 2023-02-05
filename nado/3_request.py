import requests
res = requests.get("http://www.naver.com")
print("응답코드: ", res.status_code) # 200이면 정상