print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
print("안녕하세요"[-1])  # - 를 넣으며 뒤에서 부터 센다
print("안녕하세요"[-2])  
print("안녕하세요"[0:2]) # 0과 1까지이다. 뒤에 안 들어 가는거 기억래하
print("안녕하세요"[2:])   # 뒤에 아무것도 안 쓰면 끝까지 입력 된다
print("안녕하세요"[:3])


print(len("안녕하세요"))  # 5

a="가가가가가가가가가각"
print(a.count("가"))  # 9


2 ** 3  # **하면 2의 3승으로 표현된다
15%2    # 나머지 연산자 임

7/2 #소수점까지 나온다. 4/2 도 2가 아니라 2.0 으로 float 형이 된다
7//2 #소수점 빼고 나온다
10 != 100 # 10은 100가 같지 않다


2+(2*3) # ()를 먼저 계산한다

print("15+4=",15+4)


x >= y 
x != y	# 같지 않다	


a="조중혁 김예희 조은 조한별 조한솔"
eun=a.find("은") 
sol=a.find("솔") 
print(eun) # 9
print(sol) # 17


a="그래 지금까지 잘 해 왔다"
print (a.replace("지금까지","앞으로도"))


a="hi"
a.upper()
print (a.upper())


a="HI"
a.lower()
print(a.lower())



a="그래 지금까지 잘 해 왔다"
a.split(" ") # '그래', '지금까지', '잘', '해', '왔다'





#####################################################

"{}년 {}월 {}일".format(1976,11,29)   # {}에 순서대로 숫자를 넣어 준다

"{}에 {}에 갔다".format(29,"학교") # 어렇게도 정상적으로 들어가네...

#####################################################

print("abcd".upper())
print("ADCD".lower())
print("           문자          ".strip())   # 양 옆에 있는 빈 공백을 모두 없애준다
print("           문자          ".lstrip())  # 왼쪽에 있는 빈 공백을 모두 없애준다
print("           문자          ".rstrip())  # 오른쪽에 있는 빈 공백을 모두 없애준다
print("가나다라마바사".find("다")) # "다"라는 글자가 몇번째에 있는지 출력해 준다
print("가나다라마바사".find("공")) # 해당 글자가 없을 경우 -1 을 출력해 준다
print("가나다라마가나다".rfind("다")) #왼쪽부터 세지만 맨 마지막에 있는 "다"라는 것에 위치를 찾아 준다
print("나  나 다 라 마 바 사 아".split( ))
print("가나조다라조마사바조아차".split("조")) #"조"라는 단어로 단어를 끊어준다


#####################################################

a=int(input(" > 1번쨰 숫자:"))   # int를 하지 않으면 input은 문자로 입력  받기 때문에 숫자를 입력해도 문자열로 입력이 된다


b=int(input(" > 2번째 숫자:"))

print()

print("{} + {} = {}".format(a,b,a+b))

 
#####################################################

munja = 'hello'
print(munja.upper()) # upper()로 대문자로 바꿔서 출력할수 있으나 근본이 바뀌지는 않는다
print(munja)


