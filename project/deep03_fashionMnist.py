# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:02:24 2025

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:35:27 2023

@author: family
"""



##################################################
# Fashion-MNIST 데이터셋 다운로드
from tensorflow.keras.datasets.fashion_mnist import load_data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from sklearn.metrics import confusion_matrix
import seaborn as sns
from keras.models import load_model
from PIL import Image
from tensorflow.keras.utils import plot_model
from keras.models import load_model


#(x_train, y_train), (x_test, y_test)  초기 자료

(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape,x_test.shape) #(60000, 28, 28) (10000, 28, 28)
class_names=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
         'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
y_train[:10] #[9, 0, 0, 3, 0, 2, 7, 2, 5, 5]
x_train[0]

plt.figure(figsize = (5, 5))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_train[i], cmap = 'gray')
    plt.xlabel(class_names[y_train[i]])
plt.show()

#이미지 데이터 정규화
x_trainS = x_train/255 #minmax 정규화 (x-min)/(max-min)
x_testS = x_test/255
#레이블을 onehot인코딩하기
y_trainS = to_categorical(y_train)
y_testS = to_categorical(y_test)



#검증데이터 분리. (훈련:검증)=(7:3)
x_trainS,x_valS, y_trainS,y_valS = \
  train_test_split(x_trainS,y_trainS,test_size=0.3,random_state=777)



#모델 구성

model1 = Sequential()
#Flatten :입력층
#         입력값을 1차원배열로 변경
#         28행28열 데이터를 28*28=784개의 1차원배열로 변경 입력
 #Flatten이여도 reshape 해야함
model1.add(Flatten(input_shape = (28, 28)))
model1.add(Dense(64, activation = 'relu'))
model1.add(Dense(32, activation = 'relu'))
model1.add(Dense(10, activation = 'softmax'))
model1.summary()


model1.compile(optimizer='adam', \
       loss='categorical_crossentropy',metrics=['acc'])
history1 = model1.fit(x_trainS,y_trainS, epochs=30,
        batch_size=128, validation_data=(x_valS,y_valS))  


history1.history["loss"][29] # 0.19616620242595673
history1.history["acc"][29]  #0.9278571605682373
history1.history["val_loss"][29] # 0.34093964099884033
history1.history["val_acc"][29] # 0.8887777924537659
#테스트데이터의 손실함수값, 정확도 출력하기
# [0.39299651980400085, 0.8755999803543091]
model1.evaluate(x_testS,y_testS)
#예측하기
results = model1.predict(x_testS)
np.argmax(results[:10],axis=-1)
np.argmax(y_testS[:10],axis=-1)  #원본 자료
#평가하기
#혼동행렬 출력하기
cm=confusion_matrix(np.argmax(y_testS,axis=-1),\
                    np.argmax(results,axis=-1))
cm    
#혼동행렬을 heatmap으로 출력하기

plt.figure(figsize = (7, 7))
sns.heatmap(cm, annot = True, fmt = 'd',cmap = 'Blues')
plt.xlabel('predicted label', fontsize = 15)
plt.ylabel('true label', fontsize = 15)
plt.xticks(range(10),class_names,rotation=45)
plt.yticks(range(10),class_names,rotation=0)
plt.show()


#####################################################
y_testS[0]
x_testS[0]
x_test.shape

model1.save("model/test.h5")

model= load_model('model/test.h5') 
model.evaluate(x_testS,y_testS)

