# 클라스는 소그룹인 함수들을 포함하는 큰 집합체를 의미한다. 
 








##############################################################

# 메소드를 add와 minus를 같이 만든다 


class Four_cal:
    def add(self,first,second):  # 클래스 내부에 있는 함수를 메서드(Method)라고 한다. 메서드 매개변수
        self.first=first    #메서드 수행문
        self.second=second #메서드 수행문
        
        result=self.first + self.second
        return result
    
    def minus(self,first,second):
        self.first=first
        self.second=second
        result = self.first - self.second
        return result    
        

a=Four_cal()
b=Four_cal()
print(a.add(3,4))
print(b.add(8,9)+b.minus(5,3))

##############################################################

# setdata로 받는 데이터를 분리한 후 minus에서 계산해 준다. setdata 와 minus 메소드는 다르지만 setdata에서 계산해 준 first와 second가 살아 있기에 가능하다

class Four_cal:
    def setdata(self,first,second):  # 클래스 내부에 있는 함수를 메서드(Method)라고 한다. 메서드 매개변수
        self.first=first    #메서드 수행문
        self.second=second #메서드 수행문
                
    def minus(self):
        result = self.first - self.second
        return result
    


a=Four_cal()
a.setdata(5,9)
print(a.minus())


##############################################################


class Student(): # 대문자로 선언한다

    def __init__(self):
               
        print('실행한다')

    
    def love_doimoi(self,first,second):

        self.first = first  # school.first 이다.
        self.second = second # school.second 이다.

        print('{}은 첫째딸이고, {}은 둘째 딸이다' .format(self.first, self.second))


    def internal_function(self):

        print(self.first, self.second, self.first)
    
        
  

school = Student()

school.love_doimoi('조은','조한별')

print(school.first, school.second) # 이미 위에서 school.first 와 school.second를 만들어 놓아서 활용 할수 있다.

school.internal_function() # 만들어 놓은 school.first 와 school.second를 class 내/외 모두에서 사용 할 수 있다.


##############################################################

class Student():
    
    def __init__(self):
               
        print('실행한다')
        
    def __str__(self):
        
        
        return "{}은 귀엽고 {}은 예쁘다" .format(self.first, self.second)
    
    
    def __eq__(self, other):
        print('eq을 실행했다') # 동일한 경우 실행 된다
        
    def __ne__(self, other): # not equal
        print('ne을 실행했다') 
    
    def __gt__(self, other): # greater than
        print('gt을 실행했다')
        
    def __ge__(self, other): # greater than or equal
        print('ge을 실행했다')
        
    def __lt__(self, other): # less than
        print('lt을 실행했다')
    
    def __le__(self, other): # less than or equal 
        print('le을 실행했다')
    
    
    def love_doimoi(self,first,second):

        self.first = first  # school.first 이다.
        self.second = second # school.second 이다.

        print('{}은 첫째딸이고, {}은 둘째 딸이다' .format(self.first, self.second))


    def internal_function(self):

        print(self.first, self.second, self.first)
        

school = Student()

school.love_doimoi('조은','조한별')

print(school.first, school.second) # 이미 위에서 school.first 와 school.second를 만들어 놓아서 활용 할수 있다.

school.internal_function() # 만들어 놓은 school.first 와 school.second를 class 내/외 모두에서 사용 할 수 있다.

print(str(school)) #school을 str로 변환시킨다는 뜻보다는, return 값을 받아온다는 뜻으로 봐야 할 거 같음

print(school)

school == school

print(school.__lt__(3))
school != school
school > school
school >= school
school < school
school <= school

##############################################################


import os

output= os.listdir('.') # 출력하고 싶은 위치를 넣으면 된다. 현재 폴더를 보여주고 싶으면 . 을 넣으면 된다
print('os.listdir():', output)

print('폴더와 파일 구분하기')

for path in output:
    if os.path.isdir(path): # 디렉토리일 경우 true
        print('폴더:', path)
        
    else:
        print('파일:', path)


##############################################################



