
# for  요소 변수 이름 in 반복할 수 있는 것:
# 코드


#############################################################

from itertools import count
from this import d


a=[1,2,3,4,5,6,7]

for element in a:
    print(element)

#############################################################

numbers=[273,102,402,1,492,22,102]   # 100 이상 되는 숫자만 출력해 주세요

for pandan in numbers:

    if pandan >100:
        print("100 이상의 수만 출력합니다: {}" .format(pandan) )


#############################################################

numbers=[273,103,5,32,65] 

for number in numbers:
    if number%2 ==0:
        print("{}은 짝수입니다" .format(number))
    else:
        print("{}은 홀수입니다" .format(number))
        

#############################################################


numbers=[273,103,5,32,65] 

for number in numbers:
    a= len(str(number))  # int 형은 자리수를 셀수 없다.  str로 변환 시켜 줘야 한다
    print("{}자리수 입니다" .format(a))

#############################################################

a= input("숫자를 입력해 주세요:  ")  # 자리수 세는 프로그램
b=len(a)
print("{} 자리 숫자입니다 " .format(b))


#############################################################

# list_of_list=[1,2,3], [4,5,6],[7,8,9] 를 하나 하나 꺼내서 출력해 보세요

list_of_list=[1,2,3], [4,5,6],[7,8,9]

for first_list in list_of_list:  # 이렇게 하면 first_list에 처음에는 [1,2,3] 게 들어 간다. 둘째는 [4,5,6]

    for second_list in first_list: # 이렇게 하면 second_list에 1이 들어가고, 그 다음에 2가 들어간다

        print(second_list)



#############################################################

# 짝수하고 홀수하고 분리해 list로 묶어 줘라

number= [123,4902,29,19,492,290,59,290]

jjak_moem=[]
hol_moem=[]

for hol_jjak in number:
    if hol_jjak % 2 ==0:
        jjak_moem.append(hol_jjak)
        
    else:
        hol_moem.append(hol_jjak)
        

print("짝수 모음: {}" .format(jjak_moem))
print("홀수 모음: {}" .format(hol_moem))


#############################################################

a= [(1,2,3), (3,4,6), (5,6,7)]   

for (first,middle,last) in a:   # 리스트 안에 들어간 것을 2개를 꺼낼 수 있다
    print(first)
    print(middle)
    print(last)


#############################################################
# 구구단 만들기

firstcount= 2
secondcount=1

for firstcount in range(2,10):
    for secondcount in range(1,10):

        print("{} X {}= {}"  .format(firstcount,secondcount, firstcount * secondcount) )


#############################################################

a=list(range(1,100,8))  # 1부터 99까지 8 단위로 넣어서 list에 담는다
print(a)

for i in range(10,10//2,-1 ): # 10//2로 해서 반드시 정수형으로 해야 한다. 거꾸로하려고 하면 -1로 하면 된다
    print (i)

#############################################################

testpython = [1,3,3,3,45,5,6,76,7,99]

for i in reversed(testpython):   # 반대로 돌린다
    print(i)


#############################################################

numbers=[1,2,3,4,5,1,1,1,1,6,7,8,9]


for number in numbers:

    if number > 3:
        continue  # 완전히 빠져나가서 for 문으로 나간다. 아래 print(number)를 실행하지 않는다

    print(number)


#############################################################

# {'name':'조중혁','hp':60 ...} 이렇게 나오게 해라

key_list=["name",'hp','mp','level']
vlaue_list=['조중혁',60,80,9]
new_list={}

for i in range(len(vlaue_list)): #list를 len로 가지고 오면 속에 개수를 세 준다
    new_list[key_list[i]]= vlaue_list[i]
    print(new_list)


#############################################################

# 1부터 100까지 중 1*99, 2*98처럼 계속 곱할 경우 최대가 되는 경우를 구해라

i =1
j=0
result=0
last_result=0
last_i=0
last_j=0



for i in range(1,100):

    j= 100-i

    result= i *j

    if result > last_result:

        last_i=i
        last_j=j
        last_result=result


print("최대수가 되는 경우는 : {} X {} 이며, 최대수는 {} 입니다" .format(last_i,last_j,last_result))


#############################################################

a = 0
for i in range(0,101):   # 0부터 100까지

    a += i  # [중혁] a = a + i 와 동일한거 같다

print('0부터 100까지 더한 값: {}' .format(a))

#############################################################

a = [2*x for x in range(1,5)]
print(a)

#############################################################
