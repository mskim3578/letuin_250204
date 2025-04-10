# -*- coding: utf-8 -*-



#matplot 시각화 모듈
#pip install matplotlib
#pip install seaborn



import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns
import numpy as np
plt.rcParams['axes.unicode_minus'] = False
plt.rc("font",family="Malgun Gothic")  
###-------------------------------matplotlib

###--- plot
type(vars(pd))
vlist = vars(pd).keys()
type(vlist)
# plt.plot(x, y, 스타일)``
# plt.plot(x, y, 스타일)
x1 = np.linspace(0, 10, 100)
y1 = np.random.rand(100)

# plt.plot(x1, y1, color='b', linestyle='-', marker='o', label="plt.plot()")

plt.plot(x1, y1, color='b', linestyle='-', label="plt.plot()")
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.yticks([x/10 for x in range(11)])
plt.legend()
plt.show()


###----bar
# plt.bar(x, height, 옵션)

plt.rcParams['axes.unicode_minus'] = False
plt.rc("font",family="Malgun Gothic")  

x2 = np.linspace(0, 10, 10)
y21 = (np.random.rand(10)*5) # 0  ~ 1 사이에 10개 만든다  
y21
y22 = (np.random.rand(10)*5)
y23 = (np.random.rand(10)*5)
bar_width = 0.5
# plt.bar(x2, y2, bar_width, color='red', edgecolor='black', bottom=y2)
plt.bar(x2, y21, bar_width, color='skyblue', label="y21")
plt.bar(x2+0.5, y22, bar_width, color='yellow', label="y22")
plt.bar(x2, y23, bar_width, color='red',  bottom=y21, label="y23")

plt.title("Bar Chart 예예")
plt.xlabel("Category")
plt.ylabel("Values")
plt.xticks(range(0,11, 2) , labels=["a","b","c","d","e","f"]) #range(start, end, step)
plt.yticks(range(0,11, 5))
plt.legend()
plt.show()
temp=range(0,11, 2)
###----scatter plot
#  plt.scatter(x, y, 옵션)

x3 = np.linspace(0, 10, 100)
y3 = np.random.rand(100)*10

plt.scatter(x3, y3, color='green', marker='o')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#plt.axis("off")  #x,y 축 직선 지운다 
plt.show()

###---multi  graph
y2 = np.random.rand(10)

fig = plt.figure(figsize=(5,5), num="multi graph") # 가로 세로 (5inch 의미)

plt.plot(x1, y1, color='b', linestyle='-',  label="plt.plot()")
plt.plot(x1, np.linspace(5, 5, 100), color='r', linestyle='-',  label="plt.plot()")
plt.plot(np.linspace(5, 5, 100), y1, color='r', linestyle='-',  label="plt.plot()")
plt.bar(x2, y21, color='skyblue', edgecolor='black', label="bar")
plt.scatter(x3, y3, color='green', marker='o',  label="scatter")
plt.title("Multi Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc="best")
plt.show()


###---hist
# plt.hist(data, bins, 옵션)

data = np.random.choice(10, 100) #2
# bins=30   구간 개수 조정, alpha=0.3 투명도 
plt.hist(data, bins=10, color='purple', edgecolor='black', alpha=0.3)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

###---barh
x = np.linspace(0, 10, 10)
y = np.random.rand(100)
plt.barh(x, y, color='lightcoral')
plt.title("Horizontal Bar Chart Example")
plt.xlabel("Values")
plt.ylabel("Category")
plt.show()



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
