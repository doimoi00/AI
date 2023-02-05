import re


# ca?e: cafe, case, cave


p= re.compile("^ca..") 

# . (ca.e) 은 하나의 문자를 의미한다. cafe, care, case  는 가능하나 caffe는 안 된다
# ^ (^de)은 문자열의 시작을 의미한다. desk, destination은 가능하나 fade는 안 된다
# $ (se$)은 문자열의 끝을 의미한다. case, base는 가능하나 second는 안 된다


def print_match(m):

    if m: 
        print(m.group())
    else:
        print("매칭되지 않았습니다")

m = p.match("case")