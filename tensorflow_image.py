
# minist 손글씨 이미지셋 (60000,28,28)
# CIFAR10: 10가지 분류 사물 이미지셋 (50000,32,32)

import tensorflow as tf
(mnist_x,mnist_y),_ = tf.keras.datasets.mnist.load_data() # [중혁] (mnist_x,mnist_y),_ 롤 하는 이유는 mnist가 학습셋 이미지수 60000개와 테스트 이미지 수 10000개를 이미 구분해 놓았다. 그런데 이중 학습셋 60000개만 사용하고 테스트셋은 공부하는 것이기 때문에 여기서는 사용 안하기 때문에 (mnist_x,mnist_y),_ 라는거 같다 _는 사용 안 한다는 뜻
print(mnist_x.shape, mnist_y.shape)

print("학습셋 이미지수: {} 개" .format(mnist_x.shape[0]))
print('테스트셋 이미지 수: {} 개' .format(mnist_y.shape[0]))



print('---------------------------')

(cifar_x,cifar_y),_=tf.keras.datasets.cifar10.load_data()
print(cifar_x.shape, cifar_y.shape)

# 1. 화면 출력


print(cifar_y[0:10]) 
import matplotlib.pyplot as plt
plt.imshow(cifar_x[0], cmap='gray')

# ---------------------------------------------------------

# 컨볼류션을 활용하지 않고 표 형태로 tensorflow를 돌려 보는 방법
# 텐서플로우 reshape 으로 이미지 분석하기

import tensorflow as tf
import pandas as pd

(independence, sub),_=tf.keras.datasets.mnist.load_data()
print(independence.shape, sub.shape)

independence = independence.reshape(60000, 784)
sub= pd.get_dummies(sub)

print(independence.shape, sub.shape)

# 모델을 만든다

x = tf.keras.layers.Input(shape=[784])
h=tf.keras.layers.Dense(84, activation='swish')(x) # hidden layer에서는 swish를 사용함
y=tf.keras.layers.Dense(10, activation='softmax')(h)
model=tf.keras.models.Model(x,y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')
model.fit(independence,sub, epochs=10)

pred=model.predict(independence[0:5])
print(pd.DataFrame(pred).round(2)) #  DataFrame에 넣어서 표로 만들어 준다. round(2)는 소수점 2자리에서 반올림

ds=sub[0:5]
print(pd.DataFrame(ds).round(2))

#--------------------------------------------------------------

import tensorflow as tf
import pandas as pd

(independence, sub),_= tf.keras.datasets.mnist.load_data()
print(sub.shape)
print(independence.shape, sub.shape)

independence=independence.reshape(60000,28,28,1) # 컴볼루션 레이어는 이미지 하나의 shape가 3차원이여야 한다
sub= pd.get_dummies(sub)

print(independence.shape, sub.shape)

# 모델을 만들고, CNN

x=tf.keras.layers.Input(shape=[28,28,1])
h=tf.keras.layers.Conv2D(3,kernel_size=5, activation='swish') (x) # 사이즈가 5인 3개의 특징맵을 만든다 (이미지 한장당 3개의 특징맵)
h=tf.keras.layers.MaxPool2D()(h)
h=tf.keras.layers.Conv2D(6,kernel_size=5, activation='swish') (h)
h=tf.keras.layers.MaxPool2D()(h)
h= tf.keras.layers.Flatten()(h) # flatten을 이용해 한줄로 펴서 표 형태로 바꿔준다
h=tf.keras.layers.Dense(84,activation='swish')(h)
y=tf.keras.layers.Dense(10,activation='softmax')(h)
model= tf.keras.models.Model(x,y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')

# 모델을 학습하고

model.fit(independence,sub, epochs=10)

independence_convert=model.predict(independence[0:5])
print(pd.DataFrame(independence_convert).round(2))
print(sub[0:5])

model.summary()

########################################################################

import tensorflow as tf
import pandas as pd

# 데이터를 준비합니다

(ind,sub),_=tf.keras.datasets.cifar10.load_data()
print(ind.shape, sub.shape)
sub=pd.get_dummies(sub.reshape(50000)) #표가 아니라 1차원 형태여야 get_dymmies를 사용할 수 있다
print(ind.shape,sub.shape)

# 모델을 완성합니다

x= tf.keras.layers.Input(shape=[32,32,3]) # (50000, 32, 32, 3)이기 때문에 shape=[32,32,3]로 한다
h=tf.keras.layers.Conv2D(6, kernel_size=5, activation='swish')(x) 

h=tf.keras.layers.MaxPooling2D()(h) # 위치의 크기를 절반으로 줄인다. 여기서는 28*28이 14*14로 변한다
h= tf.keras.layers.Conv2D(16, kernel_size=5, activation='swish')(h) # 이미지가 feature map(특징 맵)이 16장이 생긴다
h=tf.keras.layers.MaxPooling2D()(h) 

h=tf.keras.layers.Flatten()(h)
h=tf.keras.layers.Dense(120, activation='swish')(h)
h=tf.keras.layers.Dense(84, activation='swish')(h)
y=tf.keras.layers.Dense(10,activation='softmax')(h)

model=tf.keras.models.Model(x,y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')

model.fit(ind,sub, epochs=10)

model.summary()



