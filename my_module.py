
print(__name__) # entry file이 아닐 경우 (import 된 경우) 자신의 파일명을 출력한다, import 되는 순간이 나오기 때문에 보통 가장 상단에 나온다

a = 10
b = 20
c=0

def c(a,b):

    global c
    
    c = a+b

    return c    