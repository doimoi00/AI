
# while은 if 와 동일하지만 if는 한번만 실행되고 while은 여러번 실행 된다는 차이가 있다
#  리스트, 딕션너리, 특정 횟수 반복할때는 for을 사용하고 for로 안 될거 같은것은 while을 사용 한다


######################################################## 
# 크리스마스 날짜 세기 (while)

from time import time


day =1

while day < 25:

    print("오늘은 12월 {} 일 입니다" .format(day))
    day = day +1

if day == 25:
        print("오늘은 크리스마스입니다")

######################################################## 
# 크리스마스 날짜 세기 (for)


day =1

for day in range(0,25):

    print("오늘은 12월 {} 일 입니다" .format(day))
    day = day +1

if day == 25:
        print("오늘은 크리스마스입니다")


######################################################## 


coffee_counter=0

while coffee_counter < 10:
    
    coffee_counter = coffee_counter + 1

    print(" {} 개 팔았어요. 커피 주세요" .format(coffee_counter))

if coffee_counter ==10:

    print("이제 끝이네요. 마감입니다")


########################################################

numbers=[1,2,3,4,5,1,1,1,1,6,7,8,9]


while 1 in numbers:  # while은 for와 달리 하나 하나 떠내면서 비교하는 것이  아니라 1이 numbers에 있는지만 확인한다
    numbers.remove(1)
    print(numbers)


########################################################

# 3초 후에 특정 action 함

import time

first_time = time.time()
i = 0

while first_time + 3 > time.time():
    i = i +1
    print("{}돌고 있다" .format(i))

print("시간이 3초 지났다")


########################################################

i =0


while True:

    user_input=input("중단할까요? >>> Y나 y를  눌러 주세요")

    i  = i +1

    if user_input in ["Y","y"]: 

      

        print(" {}번 돌았습니다" .format(i))
        break

########################################################


while True:
    string_input=input("정수입력 >")
    if string_input.isdigit():  # 정수인 경우를 확인한다. 
        number_input_a = int(string_input)
        print("원의 발지름", number_input_a)
        print("원의 둘레", 2* 31.4 * number_input_a )
        
        break
    
    else:
    
        print('정수를 입력해 주세요')


########################################################

# 1+2+3 .... 해서 10000이 넘는 최초의 숫자를 얼마이며 이때 얼마를 더하고 있는가?

result=0
count=1

while result < 10000:
    
    result= result+count

    count= count + 1

print('{}이 되었을때 10000을 넘을 수 있습니다' .format(count))
print('{}가 10000이 넘는 숫자입니다' .format(result))

########################################################
# 10에서부터 역으로 1까지 더하는 문제

a = 10
c= 0

while a > 0:
    c += a # c에 A를 더한다
    a -= 1 # a는 a-1의 숫자로 재정의 한다 (조건의 변화를 주는 문장)
    print(c)

########################################################################


# 교집합 만드는 방법
def intersection(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c

a= [1,3,4,6,8,9]
b= [3,5,6,9,8,9]

print(intersection(a,b))

    
#################################################################

# 10개 전까지 주식을 구매한다

stock_buy = True
count = 0

while stock_buy:
    count = count + 1

    if count == 10:
        print("10개여서 이제는 포기한다")
        break

    print("{}개이고 구매한다" .format(count))
