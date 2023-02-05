from msilib import type_binary
from re import A
from turtle import st


num = 3
print(num)


a=1
a=a+1
a+=1
print(a)


a=1
a=a+1
a*=3  # a에 곱하기 3을 함
print(a)



print(input("----"))   # ---- 하고 터미널에서 기다리고 있음

a = input("첫번째 숫자로 입력해 주세요")
b=input("두번째 숫자를 입력해주세요")
print(a+b)  # input함수는 모두 문자형이기 때문에 숫자 더하기가 안 된다. 파이썬튜어와 정식으로 py 만들어서하면 잘 되는데 여기서는 잘 안 되네

a= float(input("첫번째 숫자를 입력해 주세요"))  # 더하기를 하기 위해서는 int()나  float()로 변경해 줘야 한다, 단 int()는 소수가 들어가면 에러 난다
b=float(input("두번째  숫자를 입력해 주세요"))
print(a+b)  

------------------------

str(123456) # 문자열로 변환
type(123456)

-------------------------

string_input=input("숫자를 입력해 주세요 >>")
num_input=float(string_input)

print()
print(num_input, "inch")
print(num_input*2.54,"cm")


---------------------------

# 원의 둘레와 넓이 구하는 방법

string_input=input("반지름을 입력해 주세요")
num_input=float(string_input)

print("반지름:",num_input)
print("둘레:", num_input*2*3.14)
print("넓이:",num_input*num_input*3.14)


-----------------------------

a=input("문자열을 입력해 주세요:")
b=input("문자열을 입력해 주세요:")

print(a,b)
a,b=b,a

print(a,b)


