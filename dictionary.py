
dic= { "키A":"값A", 
    "키B":"값B",
    "아빠":"조중혁",
    1:3,
    1.5:[2,3,4,2,1],
        }

print(dic["키B"])
print(dic["아빠"])
print(dic[1])
print(dic[1.5])
dic[1]=5 # dictionary 변경하는 방법

print(dic[1])

for key in dic: # for를 돌면서 key만 가지고 온다. 키값은 안 가지고 온다
    print("{}:{}" .format(key,dic[key]))


print()
dic["도이모이"]="조중혁" # dictionary 를 추가하는 방법

for key in dic: # for를 돌면서 key만 가지고 온다. 키값은 안 가지고 온다
    print("{}:{}" .format(key,dic[key]))

print()

del dic["도이모이"] # dictionary 를 삭제하는 방법

for key in dic: # for를 돌면서 key만 가지고 온다. 키값은 안 가지고 온다
    print("{}:{}" .format(key,dic[key]))


########################################################

myhomes={'아빠':'조중혁','엄마':'김예희','아들':'조한솔'}

for myhome in myhomes:

    print("{}는 키이고 {}는 값이다" .format(myhome,myhomes[myhome] ))




########################################################


# list 안에 dictionary를 넣을 수 있다


pets=[

    {'name':'구름','age':5},
    {'name':'초코','age':29},
    {'name':'마리','age':5}

]

print("우리동네 애완동물")

for pet in pets: # 첫번쨰 pet에는 {'name':'구름','age':5}가 들어 간다

    print('{}는 {}살이다' .format(pet['name'],pet['age']))


########################################################

# list 안에 dictionary를 넣을 수 있다


myhomes=[{'name':'아빠','age':47},{'name':'엄마','age':43},{'name':'아들','age':12}]

for myhome in myhomes:
    print('{}는 {}살입니다' .format(myhome['name'],myhome['age']))

########################################################
# numbers에 있는 숫자를 카운트해서 {1:2} 처럼 표시해라


numbers=[1,2,3,3,4,2,3,4,4,2,2,2,1,1,25,6,7,1,1,1,1,23,35,3,2,3,4,5] 
counter={}

for number in numbers:

    if number in counter:
        counter[number] +=1 # {1:3} 에 value에 +1을 한다

    else:
        counter[number]=1

print(counter)


########################################################

# 평탄화 작업을 해봐라

character = {
    'name':'기사',
    'lever':12,
    'item':{'sword':'불꽃의 검', 'armor':'sexnal armed'},
    'skill':['push','pull','sex']
    
}



for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{}:{}"  .format(k,character[key][k]))  #  character['item']['sword'] 이렇게 이중으로 해서 가지고 올 수 있다
    elif type(character[key]) is list:
        for item in character[key]:
            print("{}:{}"  .format(key,item))

    else:
        print("{}:{}"  .format(key,character[key]))

########################################################

marks = {"sungin":80, "joonghyuk":100,"sangsun":70}

for mark in marks:
    if marks[mark] >90:
        print("{} {} pass" .format(mark, marks[mark]))
    else:
        print("{} {} fail" .format(mark, marks[mark]))



########################################################

myhomes={'아빠':'조중혁','엄마':'김예희','아들':'조한솔'}

for myhomekey in myhomes.keys():

    for myhomevalue in myhomes.values():

        print("{}는 {}이다." .format(myhomekey,myhomevalue))

########################################################

dic_family={'아빠':"조중혁", '엄마':'김예희','아들':'조한솔'}

a=dic_family.items()
print(a)

for i,j in a:
    print("{}는 {}입니다"  .format(i,j))


