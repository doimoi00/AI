import pandas as pd
s=pd.Series(['banana',42])
# print(s)
# print(s.shape)

s= pd.Series(['wes mckinney','creator of pandas'])
s=pd.Series(['wes mckinney','creator of pandas'], index=['person','who']) #index를 사용해 첫줄의 명칭을 정해 줄 수 있다

# print(s)

# 데이터프레임을 만들기 위해서는 dictionary를 DataFrame 클래스에 전달해야 한다

scientists=pd.DataFrame(
    data={ 
    'Occupation': ['chemist','statistician'],
    'Born': ['1920-07-08','1876-06-13'],
    'Died': ['1958-04-16','1937-10-16'],
    'Age':[37,61]},
    
    index=['Rosaline Franklin','William Gosset'],
    columns=['Occupation','Born','Died','Age']
)

print(scientists)

print('----------------------------------------')

first_row=scientists.loc['William Gosset']
print('first_row',first_row)

print('----------------------------------------')

# print('first_row.index',first_row.index)

# print('----------------------------------------')
# 
# print('first_row.values',first_row.values)
# 
# print('----------------------------------------')
# 
# print(first_row.keys())

ages=scientists['Age']
print(ages)


print('평균',ages.mean())
print('최소:', ages.min())
print('최고:', ages.max())
print('표준편차',ages.std())

################################################################################## 

scientists=pd.read_csv('C:/Users/doimo/pythonDataWorkspace/doit_pandas-master/doit_pandas-master/data/scientists.csv')
ages=scientists['Age']
print(ages)

print('ages.max',ages.max())

print('평균보다 나이가 많은 사람',ages[ages>ages.mean()])
