import re


# ca?e: cafe, case, cave


p= re.compile("ca..") 

# . (ca.e) 은 하나의 문자를 의미한다. cafe, care, case  는 가능하나 caffe는 안 된다
# ^ (^de)은 문자열의 시작을 의미한다. desk, destination은 가능하나 fade는 안 된다
# $ (se$)은 문자열의 끝을 의미한다. case, base는 가능하나 second는 안 된다


def print_match(m): 

    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반황
        print("m.string:", m.string)   # m.string()이 아니다. 함수가 아님. 이유는 모르겠다. 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():",m.span()) # 일치하는 문자열의 시작 / 끝 index


    else:
        print("매치 되지 않았습니다")

m = p.search("good careless") # 주어진 문자열 중에 일치하는 것이 있는지 확인한다
print_match(m)

print(" ")

list=p.findall("good care cafe") #  일치하는 모든 것을 리스트 형태로 반환
print(list)