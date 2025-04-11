# -*- coding: utf-8 -*-



#matplot 시각화 모듈
#pip install matplotlib
#pip install seaborn



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
fig = plt.figure(figsize=(5,5), num="multi graph")
plt.rcParams['axes.unicode_minus'] = False
plt.rc("font",family="Malgun Gothic")  

###-------------------------------matplotlib
###--- plot


# plt.plot(x, y, 스타일)
x1 = np.linspace(0, 10, 100) # 0 ~ 9 까지의 수를 100개 
y1 = np.random.rand(100) # 0 ~ 1까지의 수를 100개개

# plt.plot(x1, y1, color='b', linestyle='-', marker='o', label="plt.plot()")
plt.rcParams['axes.unicode_minus'] = False
plt.rc("font",family="Malgun Gothic")
plt.plot(x1, y1, color='b', linestyle='-', label="plt.plot()")
plt.title("Line Plot 자료 ")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xticks([x for x in range(0,11)] ,
           labels=[str(x)+"A" for x in range(0,11)])
plt.yticks([x/10 for x in range(0,11)])
plt.legend()
plt.show()


###----bar
# plt.bar(x, height, 옵션)

plt.figure(figsize=(5,5), num="바차트")
x2 = np.linspace(0, 10, 10)  # 0 ~ 10 사이에 10개의 수
y2 = (np.random.rand(10))  # 0  ~ 1 사이에 10개 수  
y21 = (np.random.rand(10))  # 0  ~ 1 사이에 10개 수 
y22 = (np.random.rand(10))  # 0  ~ 1 사이에 10개 수 
# plt.bar(x2, y2, bar_width, color='red', edgecolor='black', bottom=y2)
plt.bar(x2, y2,  color='skyblue', edgecolor='black', label="y2")
plt.bar(x2, y21,  color='yellow', edgecolor='black', label="y21",bottom=y2)
plt.bar(x2, y22,  color='red', edgecolor='black', label="y22", bottom=y2+y21)
plt.title("Bar Chart ")
plt.xlabel("Category")
plt.ylabel("Values")
plt.legend()
plt.show()



###----scatter plot
#  plt.scatter(x, y, 옵션)
x3 = np.linspace(0, 10, 100)
y3 = np.random.rand(100)
plt.scatter(x3, y3, color='green', marker='o')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

###---multi  graph



plt.plot(x1, y1, color='b', linestyle='-',  label="plt.plot()")
plt.bar(x2, y2, color='skyblue', edgecolor='black', label="bar")
plt.scatter(x3, y3, color='green', marker='o',  label="scatter")
plt.title("Multi Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc="best")
plt.show()


###---hist
# plt.hist(data, bins, 옵션)

data = np.random.choice(10, 100) #2
# bins=10   구간 개수 조정, alpha=0.3 투명도 
plt.hist(data, bins=10, color='purple', edgecolor='black', alpha=0.3, )
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

###---barh
x = np.linspace(0, 10, 10)
y = np.random.rand(10)
plt.barh(x, y, color='lightcoral')
plt.title("Horizontal Bar Chart Example")
plt.xlabel("Values")
plt.ylabel("Category")
plt.show()




###----Pie Chart
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 35, 15]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', 
    colors=['gold', 'lightblue', 'lightcoral', 'lightgreen'])
plt.title("Pie Chart Example")
plt.show()



###----box plot
#  plt.boxplot(data, 옵션)
data = [np.random.randn(100), np.random.randn(100) + 2]
plt.boxplot(data, labels=['Group 1', 'Group 2'], 
patch_artist=True)
plt.title("Box Plot Example")
plt.show()



###--- heatmap
# sns.heatmap(data, 옵션)
import seaborn as sns
data = np.random.rand(5,5) # shape이 (5,5) 에 값을 대입하여 큰수를 color로 표현한다 
data.shape
# (5,5) 좌표의 값이 0 ~ 1 수이고 큰수 일 수록 빨강색으로 표시된다 

sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title("Heatmap Example")
plt.show()
'''
data
array([[0.63748206, 0.37562554, 0.89967241, 0.32849748, 0.24600117],
       [0.51874804, 0.53793694, 0.6258997 , 0.03524937, 0.32276094],
       [0.60830768, 0.63371564, 0.94818485, 0.34676995, 0.58470962],
       [0.71889598, 0.51113683, 0.69197056, 0.60150562, 0.62953753],
       [0.06677481, 0.61731743, 0.54237012, 0.13600106, 0.85049451]])
>>>

'''

x2 = np.linspace(0, 10, 10)
y2 = np.random.rand(10)
plt.bar(x2, y2, color='skyblue', edgecolor='black')
plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()





###--- 여러개 그래프
y2 = np.random.rand(10)
# #  fig, axes = plt.subplots(rows, cols)
fig, ax = plt.subplots(2, 2, figsize=(5, 5))
data = np.random.randn(1000)
ax[0, 0].plot(x1, y1)
ax[0, 0].set_title("Line Plot")

ax[0, 1].bar(x2, y2)
ax[0, 1].set_title("Bar Chart")

ax[1, 0].hist(data, bins=10, color='purple', edgecolor='black', alpha=0.7)
ax[1, 0].set_title("Histogram")

ax[1, 1].scatter(x3, y3)
ax[1, 1].set_title("Scatter Plot")

plt.tight_layout()
plt.show()


#자동차 연비데이터의 mpg 값을 히스토그램으로 출력하기
df=sns.load_dataset("mpg")
df.info()
'''
mpg : 연비
cylinders : 실린더 수
displacement : 배기량
horsepower : 출력
weight : 차량무게
acceleration : 가속능력
model_year : 출시년도
origin : 제조국
name : 모델명
'''
#DataFrame plot 히스토그램 출력
# width= 간격
df['mpg'].plot(kind='hist', width=1, bins=20)
plt.title('MPG 히스토그램')
plt.xlabel('mpg(연비)')
plt.show()
#weight, mpg 산점도 출력 
#DataFrame.plot(kind="scatter") : 그래프 종류
# x='mpg' : x축의 사용될 컬럼명
# y='weight' : y축의 사용될 컬럼명
# s=50 : 점의 크기지정
df.plot(kind='scatter', x='mpg', y='weight',s=50, c='coral',
        figsize=(10,5))

plt.scatter(df['mpg'], df['weight'], c='coral', s=50)
plt.xlabel('mpg')
plt.ylabel('weight')
plt.show()


# 제조국별 자동차 건수 조회하기
df['origin'].unique()
df['origin'].value_counts()

df.origin.unique()
df.origin.value_counts()


plt.pie(df.origin.value_counts(), labels=df.origin.unique(), autopct='%1.1f%%', 
    colors=['gold', 'lightblue', 'lightcoral', 'lightgreen'])
plt.title("Pie Chart Example")
plt.show()


df.shape #(398,9)
#모든 컬럼의 자료형을 조회하기
df.dtypes

#데이터의 mpg,weight 컬럼의 최대값 조회하기
df.mpg.max() #46.6
df.weight.max() #5140
df[['mpg','weight']].max()

#최대 연비를 가진 자동차의 정보 조회하기
df[df['mpg']==df['mpg'].max()]
df.loc[df['mpg']==df['mpg'].max()]
df.iloc[df['mpg'].idxmax()]

# 데이터의 컬럼간의 상관계수 조회하기
df[['mpg','weight']].corr()
