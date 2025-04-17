# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 12:01:13 2025

@author: Admin
"""

#MNIST 데이터를 이용하여 숫자를 학습하여 숫자 인식하기.
#MNIST 데이터셋 다운받기

from tensorflow.keras.datasets.mnist import load_data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from PIL import Image
from keras.models import load_model
from sklearn.metrics import \
    classification_report,confusion_matrix
    
(x_train, y_train),(x_test, y_test)=load_data(path='mnist.npz')
tempimg = x_test[1]
im = Image.fromarray(tempimg)
im.save('num.jpg', 'jpeg')

#0~59999 사이의 임의의 수 3개
random_idx = np.random.randint(60000,size=3) 
for idx in random_idx :
    img = x_train[idx,:]
    label=y_train[idx] 
    plt.figure()
    plt.imshow(img)
    plt.title\
  ('%d-th data, label is %d' % (idx,label),fontsize=15)
  
#검증데이터 생성 : 학습 중간에 평가를 위한 데이터  
x_train,x_val,y_train,y_val = train_test_split\
    (x_train,y_train,test_size=0.3, random_state=777)  
    
# 데이터 정규화
#MinMax normalization 정규화
#현재데이터 : min:0, max=255
x_train = (x_train.reshape(42000,28*28))/255 
x_val = (x_val.reshape(18000,28*28))/255
x_test = (x_test.reshape(10000,28*28))/255

fy_train=to_categorical(y_train)
fy_val=to_categorical(y_val)
fy_test=to_categorical(y_test)

model = Sequential([
    Dense(units=64,activation='relu',input_shape=(784,)),
    Dense(units=32,activation='relu'),
    Dense(units=10,activation='softmax')    #이중분류 사용. 
    ])
model.compile(optimizer="adam", 
              loss='categorical_crossentropy',
              metrics=['acc'])

history = model.fit(x_train,fy_train,
                    epochs=30,
                    batch_size=127,
                    validation_data=(x_val,fy_val))


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
plt.plot(history.history['acc'], 'b-', 
         label='acc') 
plt.plot(history.history['val_acc'], 'r--',\
         label='val_acc')
plt.xlabel('Epoch') 
plt.ylim(0.7, 1) 
plt.legend()

results = model.predict(x_test)

#한개이미지 예측하기
















    
