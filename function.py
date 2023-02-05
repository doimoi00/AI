# 함수를 선언하는 부분


def 함수이름(매개변수1,매개변수2,매개변수3):

    내용
    내용

    return 매개변수1 + 매개변수2


# 함수를 호출하는 방법
함수이름(매개변수1,매개변수2,매개변수3)


###########################################################################

def hello():

    print('안녕중혁')
    print("중혁 안녕")
    print('한솔이랑 놀때가 제일  좋았어')


hello()

###########################################################################




def print_n_times(value,n):

    for ntimes in range(1,n+1):

        print('{}, {}번째입니다.' .format(value,ntimes))

        
print_n_times('이제 살만해진거 같다',5)

print()

###########################################################################

def function_test(일반매개변수A,일반매개변수B, *가변매개변수, 기본매개변수A=10, 기본매개변수B=20):

    print(일반매개변수A, 일반매개변수B) # 1 2

    print(가변매개변수) # (3, 4, 5, 6, 7, 8, 9, 10)

    print(기본매개변수A, 기본매개변수B) # 10 20

function_test(1,2,3,4,5,6,7,8,9,10)



def sum_all(start,end):

    j =0

    for i in range(start,end+1):
        
        j = i + j

    return j

print(sum_all(1,10)) # 55

###########################################################################

def call_10_time(func):
    
    for i in range(10):

        j='중혁'

        func(i,j)

def print_hello(number, name):

    print('안녕하세요 {}번째 입니다' .format(number))
    print('저는 {}라고 합니다'  .format(name))


call_10_time(print_hello) # 자기가 호출하는 것이 아니라 남이 호출해 준다고 해서 callback 함수라고 한다

###########################################################################


def call_10_times(func):

    for i in range(10):

        func(i)

call_10_times(lambda number: print('안녕하세요',  number)) # lambda 뒤에는 한줄의 코드를 입력할 수 있으며, 한줄의 코드를 자동으로 return 해 준다. 


###########################################################################

# filter 사용하기

def jjaksu(number):

    if number % 5  == 0:

        return number
    
    # return number % 5 ==0  # filter 함수를 사용할때는 return 이 bool이여야 한다

a = list(range(100))
b = filter(jjaksu,a)

for i in b:
    print(i)


###########################################################################

# 위에 filter 사용하기를 lambda를 이용해서 코드를 줄일 수 있다

a = list(range(100))
b = filter(lambda number: number % 2 ==0, a)

print(list(b))


###########################################################################

# map 사용하기, 정확하게 map 함수가 뭔지 잘 모르겠다

def double_double(number):

    return  number * number


a = list(range(100))

print(list(map(double_double,a))) # map은 list를 기반으로 새로운 list를 만들때 사용 한다


###########################################################################

# 위에 map 사용하기를 lambda를 이용해서 코드를 줄일 수 있다


a = list(range(100))
print(list(map(lambda number: number * number, a)))

###########################################################################

while True:
    
    try:
        
        a= int(input('숫자를 입력해 주세요>>>'))    
        print(a)
        break
        
    except:
        pass # 에러가 발생하면 무시한다
###########################################################################    

list_input_a=["52",'조은', '292', '292',32,'조중혁','28282']

numberplus=[]

for a in list_input_a:
    
    try:         
        intnumber =int(a)
            
        numberplus.append(intnumber)
        
    except:
    
        numberplus.append('이건 에러야')
          
print(numberplus)   
    
###########################################################################    
    
def write_text_file(filename,text):
    
    try:
        
        file=open(filename,'w')
        file.write(text)
        fiel.sfdadsf
        return
    
    except Exception as e: # 에러 내용을 잡아서 print로 보여 준다 
        
        print(e) 
        
    finally:
        
        file.close()
        print('finally 실행 되었나?')
        
        
write_text_file('중혁이파일.txt','안뇽안뇽')
    
###########################################################################    
    
try:
    a=[ 281,302,214,320]
    number= int(input('숫자를 입력해 주세요'))
    print(a[number])
    
except ValueError as e:
    
    print('값에 문제가 있습니다')
    
except IndexError as e:
    
    print(' 0부터 4까지 입력해 주세요')
    
except Exception as e:
    
    print('알수 없는 에러입니다')    

###########################################################################

students = [{'name':'조중혁','성격':42,'나이':47,'학년':42},
            {'name':'조한솔','성격':22,'나이':13,'학년':12}]

def 총점(student):
    return student['성격'] + student['나이'] +\
        student['학년'] 
        
def 평균(student):
    return 총점(student)/3

def 출력(student):
    print(student['name'], 총점(student), 평균(student), sep="\t")
    
print('이름', '총점', '평균', sep='\t')

for student in students:
    출력(student)


###########################################################################    

# 재귀 함수


def count(n):

    if n > 3:
        return # count(1) 이 끝나 버린다. 결국 프로그램 종료
    
    print('출력:', n)

    count(n+1)

count(1)

###########################################################################    


def hello(count):

    if count == 0:

        return
    
    else:

        print('출력한다', count)

        count= count -1

        hello(count)

hello(10)

###########################################################################    

# 함수에 함수 전달하기

def english(help):
    help()

def help():
    print("도와주러 왔습니다")

english(help)

######################################################################



# 함수에서 데이터 반환 받기

def math():
    name ="광수"
    return name

who = math()
print (who)

######################################################################

# 함수에서 여러 데이터 반환받기 

def multi():
    return "a", "b"

result=multi() # 듀플로 들어 간다
print(result) 

######################################################################

def english(help):
    help()
    
def help():
    print("도와주러 왔다")
    

english(help)

######################################################################

def math():
    name='광수'
    return name

who = math()
print(who)