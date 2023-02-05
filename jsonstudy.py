# 숫자: 10,20,30,40
# 문자열: "안녕하세요", "제품", "102010"
# 불: true, false
# null: null
# 배열: [10,92,"안녕하세요", true]
# 객체:
# {"키A":291,
#  "키B":"값"
#  "키C":true,
#  "키D":[12,41],
#  "키E":{"name":42}
# }


import logging
import urllib.request as request
import json

json_string=request.urlopen("https://api.github.com/repositories").read()

output = json.loads(json_string)  # 외부에 있는 문자열을 파이썬의 자료형으로 변환
# print(output)

print()

text=json.dumps(output) # 파이썬 자료형을 json 문자열로 변환 (일반 글자로 변환해 사용할수도 있음)

# print(text)


for item in output:
    print(item["name"])
    print(item["full_name"])
    print(item["owner"]["login"]) # itme list > ower > login 을 찾아 달라는 뜻
    print()
    