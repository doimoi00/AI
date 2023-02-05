#%%
import pandas as pd



df = pd.read_csv('C:/Users/doimo/pythonDataWorkspace/doit_pandas-master/doit_pandas-master/data/gapminder.tsv', sep='\t')

# print(df.shape) # (1704,6) 출력
# print(df.columns)
# print(df.dtypes) 
# print(df.head())

subset = df[['country', 'continent', 'year']] # df로 subset을 만들어서 print할 수 있다
# print(subset.head())

number_of_rows=df.shape[0] # 마지막 행을 출력하기 위해서는 rows 개수를 구한 다음에 -1을 빼 주고 loc를 가져와야 한다. df.shape[0]은 rows 개수이고, df.shape[1]은 columns 개수이다.
last_row_index=number_of_rows -1
# print(df.loc[last_row_index])

# print(df.tail(n=1)) # 이렇게 해도 마지막 row을 가지고 올 수 있지만 모양이 약간 다르다

subset_loc = df.iloc[0:5]  # df.loc[2:5] : 2행부터 5행 가져오기, df.iloc[2:5] : 2행부터 4행 가져오기

# print(subset_loc = df.iloc[0:5])
subset_tail = df.tail(n=1)

# print(subset_loc)


# print(type(subset_loc)) # loc는 반환하는 자료형이 Series (pandas에서 Series 는 1차원 배열의 자료구조)
# print(type(subset_tail)) # tail은 반환하는 자료형이 DataFram (pandas에서 DataFrame은 2차원 배열의 자료구조입)

# range 구문으로 데이터 추출하기

small_range=list(range(5)) # [0, 1, 2, 3, 4]

subset = df.iloc[:,small_range] # row는 전체, columns은 0~4까지
# print(subset)

# print(df.groupby('year')['lifeExp'].mean()) # 연도별 lifeExp 열의  평균 계산함, grouby('year')를 하면 연도별로 그룹화한 country, continent ... gdpPercap열을 모은 데이터프리엠을 얻을 수 있음. 이중 ['lifeExp']을 가지고 온 후 평균을 구해주는 메소드 사용 함
# print(df.groupby('year')['lifeExp'].nunique()) # 평균이 아닌 개수를 구해 줌


import matplotlib.pyplot as plt

global_yearly_life_expectancy=df.groupby('year')['lifeExp'].mean()
# print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()





# %%
