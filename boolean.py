from ast import If
from fcntl import F_SEAL_SEAL
from http.client import ImproperConnectionState
from operator import truediv
from tkinter.tix import Tree
from turtle import st


10 == 100 # 거짓
10 !=100 # 10은 100과 같지 않다. 참
10 > 100 # 거짓
10 < 100 # 참
10 >= 20# 거짓

x=15
10 < x < 20 # 참

True and True # True
True and False # False
False and True  # False
False and False # False

True or True # True
True or False # True
False or True # True
False or False # False

####################################################

age = 20

if  age < 19:
    age=age+1
    print(age)

else: 

    age= age-1
    print(age)

    
####################################################


number = int(input("입력해주세요>>"))

if number ==0:
    print("0입니다")

if number >0:
    print("양수입니다")

else:
    print("음수입니다")


####################################################

import datetime

now = datetime.datetime.now()


if now.hour <12:
    print("현재 시간은 {}시로 오전입니다" .format(now.hour))

else:
    print("현재 시간은 {}시로 오후입니다" .format(now.hour))

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

####################################################


import datetime

now = datetime.datetime.now()


if now.hour < 12:
    print("현재 시간은 %d시로 오전입니다" %now.hour) # %d나 %s로도 가능하고 .format으로도 가능하다

else:
    print("현재 시간은 {}시 {}분이며 오후입니다" .format(now.hour, now.second))


####################################################

number = int(input("숫자를 입력해 주세요 >>"))

holjjak= number%2

if holjjak ==0:
    print("짝수입니다")

else:
    print("홀수입니다")

#####################################################

number= input("정수를 입력해 주세요 >>>")

last_charater = number[-1]

if last_charater in [0,2,4,6,8]:
    print("짝수입니다")

else:
    print("홀수입니다")

#####################################################

bool(0) # False
bool(0.0) # False
bool(0.1) # True
bool(-1) # True
bool([1,2,3]) True
bool() # False

#####################################################

number=12

if number !=0: 
    print("처리를 한다")

else:
    print("처리를하지 않는다")


#####################################################

number=12

if number:  # 이렇게하면 if 뒤에 있는 것이 참인지  거짓인지 (bool)을 파악한다
    print("처리를 한다")

else:
    print("처리를하지 않는다")


#####################################################

number=0

if number != 0:
    pass  # 나중에 프로그램 짜려고 할때 pass를 넣어 놓는다

else:
    pass

#####################################################

input_age=int(input("태어난 해를 입력해 주세요"))

age_devide=int(input_age%12)

if age_devide ==0:
    print("원숭이")

elif age_devide ==1:
    print("닭")

elif age_devide == 2:
    print("개")

elif age_devide ==3:
    print("돼지")

elif age_devide ==4:
    print("쥐")

elif age_devide == 5:
    print("소")

elif age_devide ==6:
    print("범")

elif age_devide ==7:
    print("토끼")

elif age_devide == 8:
    print("용")

else:
    print("개돼지")


