# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:15:57 2025
pip install tensorflow
@author: Admin
"""
import pandas as pd
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import numpy as np



url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/"
red = pd.read_csv(url+'winequality-red.csv', sep=';') #red 와인 정보
white = pd.read_csv(url+'winequality-white.csv', sep=';') #white 와인 
red.info() #1599
white.info()  #4898

'''
1 - fixed acidity : 주석산농도
2 - volatile acidity : 아세트산농도
3 - citric acid : 구연산농도
4 - residual sugar : 잔류당분농도
5 - chlorides : 염화나트륨농도
6 - free sulfur dioxide : 유리 아황산 농도
7 - total sulfur dioxide : 총 아황산 농도
8 - density : 밀도
9 - pH : ph
10 - sulphates : 황산칼륨 농도
11 - alcohol : 알코올 도수
12 - quality (score between 0 and 10) : 와인등급
'''
#type 컬럼 추가
#red와인인경우 type컬럼에 0, white와인인 경우 
# type컬럼에 1 을 저장하기.
red["type"]=0   # label 
white["type"]=1
#red,white 데이터를 합하여 wine 데이터에 저장하기
wine = pd.concat([red,white])
wine.info()
wine.head()

#wine 데이터를 minmax 정규화하여 wine_norm 데이터에 저장
wine.min()
wine.max()
wine_norm = (wine-wine.min()) / (wine.max()-wine.min())
wine_norm
'''
      fixed acidity  volatile acidity  citric acid  ...   alcohol   quality  type
0          0.297521          0.413333     0.000000  ...  0.202899  0.333333   0.0
1          0.330579          0.533333     0.000000  ...  0.260870  0.333333   0.0
2          0.330579          0.453333     0.024096  ...  0.260870  0.333333   0.0
3          0.611570          0.133333     0.337349  ...  0.260870  0.500000   0.0
4          0.297521          0.413333     0.000000  ...  0.202899  0.333333   0.0
'''
wine_norm.head()
wine_norm.min()
wine_norm.max()
type(wine_norm)
wine_norm["type"].head()
wine_norm["type"].tail()
# wine_norm 데이터를 섞어 wine_shuffle 데이터에 저장하기.
import numpy as np
#sample() : 임의로 표본추출을 위한 함수. 
#frac=1 : 표본추출의 비율. 1은 100%. 
wine_shuffle = wine_norm.sample(frac=1)
wine_shuffle["type"].head(10)
wine_shuffle["type"].tail(10)
wine_shuffle.info()


#wine_shuffle 데이터를 배열데이터 wine_np로 저장
wine_np = wine_shuffle.to_numpy()
type(wine_np)
wine_np.shape

# 데이터 분리 80:20
train_idx = int(len(wine_np)*0.8)
train_idx
ttrain_x,ttrain_y=wine_np[:train_idx,:-1],wine_np[:train_idx,-1]
# [:80,]
ttest_x,ttest_y=wine_np[train_idx:,:-1],wine_np[train_idx:,-1]
# [80:,]
ttrain_x.shape
ttest_x.shape
ttrain_y.shape
ttest_y.shape

train_x=ttrain_x
test_x=ttest_x

train_y =tf.keras.utils.to_categorical(ttrain_y,num_classes=2)
test_y = tf.keras.utils.to_categorical(ttest_y,num_classes=2)
test_y

#모델 생성
model = Sequential([
    Dense(units=48,activation='relu',input_shape=(12,)),
    Dense(units=24,activation='relu'),
    Dense(units=12,activation='relu'),
    Dense(units=2,activation='sigmoid')    #이중분류 사용. 
    ])
model.summary()

#binary_crossentropy : 이중분류에서 사용되는 손실함수
#                      레이블을 onehot 인코딩 필요
model.compile(optimizer="adam", 
              loss='binary_crossentropy',
              metrics=['accuracy'])
#validation_split=0.25 : 25%의 데이터를 검증데이터로 사용    
history = model.fit(train_x,train_y,
                    epochs=25,
                    batch_size=32,
                    validation_split=0.25)
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
#'b-' : blue 실선
plt.plot(history.history['loss'], 'b-', label='loss')
#'r--' : red, 점선
plt.plot(history.history['val_loss'], 'r--', 
         label='val_loss') 
plt.xlabel('Epoch')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], 'b-', 
         label='accuracy') 
plt.plot(history.history['val_accuracy'], 'r--',\
         label='val_accuracy')
plt.xlabel('Epoch') 
plt.ylim(0.7, 1) 
plt.legend()






















