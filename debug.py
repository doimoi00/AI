import tensorflow as tf
import pandas as pd
import numpy as np


# 실행할때마다 같은 결과를 출력하기 위해 설정하는 부분

np.random.seed(3) # ramdom.seed는 램덤하게 섞기는 하지만 실행시킬 때마다 동일하게 섞어준다
tf.random.set_seed(3) # [중혁] 인터넷 찾아보니 랜덤함수를 사용할떄 기준이 되는 seed를 정할수 있다고 하는데 모르겠다

data_set=np.loadtxt('C:/Users/doimo/pythonDataWorkspace/080228-master/080228-master/deeplearning/dataset/ThoraricSurgery.csv', delimiter=',')

# 환자의 수술 기록과 수술 결과를 x와 y로 저장

print(data_set.shape)

independence=data_set[:,0:17]

sub=data_set[:,17]

x=tf.keras.layers.Input(shape=[17])
h=tf.keras.layers.Dense(10,activation='swish')(x)  # 히든 레이더를 만든다
y=tf.keras.layers.Dense(1)(h)
model=tf.keras.models.Model(x,y)
model.compile(loss='mse')

model.fit(independence,sub,epochs=1000)






