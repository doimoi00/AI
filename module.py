import math as mathmatics
print(mathmatics.pi)
print(mathmatics.sin(10))

from math import pi,sin # 이렇게도 할 수 있다. 
print(pi*2)
print(sin(10)*2)

##############################################################



import sys
print(sys.argv)


##############################################################


from datetime

now=datetime.now()

datetime(now.year)from datetime import datetime

now=datetime.now()
print(now.year)
print(now.month)

##############################################################

import time

print('안녕하세요')
time.sleep(3)

print('3초 후 나온다')

##############################################################

from urllib import request

target = request.urlopen('http://www.naver.com')  # naver 코드를 가지고 온다

content=target.read()
print(content)

##############################################################

import os

output= os.listdir('.') # 출력하고 싶은 위치를 넣으면 된다. 현재 폴더를 보여주고 싶으면 . 을 넣으면 된다
print('os.listdir():', output)

print('폴더와 파일 구분하기')

for path in output:
    if os.path.isdir(path):
        print('폴더:', path)
        
    else:
        print('파일:', path)