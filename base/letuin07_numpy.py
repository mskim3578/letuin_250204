## numpy :행렬, 통계관련기본함수,배열 기능 제공하는 모듈
import numpy as np

#배열 생성
#np.arange(15) : 0 ~ 14까지의 숫자를 1차원 배열로 생성
#reshape(3,5) : 3행5열의 2차원배열로 생성.
#               배열 갯수가 맞아야 함.
x= np.arange(15)
a = x.reshape(3,5)
a  #0~14까지의 숫자를 3행 5열의 2차원배열로 생성
type(a)
#배열 요소의 자료형
a.dtype  #int32 => 32비트, 4바이트
#배열 형태
a.shape #(3,5) : 3행 5열 2차원 배열


np.arange(15).shape #(15,) 1차원배열 [1,2,3]
np.arange(15).reshape(15,1).shape #(15, 1) 2차원배열  [[1,2,3]]

#배열의 차수
a.ndim  #2차원
x.ndim 
np.arange(15).ndim #1
#배열의 요소의 바이트 크기
a.itemsize  #8
#배열의 요소의 갯수
a.size 
np.arange(15).size

#리스트로 배열 생성하기
b=np.array([6,7,8])
b
type(b)
#튜플로 배열 생성하기
c=np.array(6,7,8)  #오류
c=np.array((6,7,8))  
c
type(c)


#리스트로 2차원 배열 생성하기
d=np.array([[6,7,8],[1,2,3]])
d
type(d)
#0으로 초기화된 3행 4열 배열 e 생성하기
e=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
e
e.shape


#zero값  setting
e=np.zeros((3,4))
e
e.shape

# 모든 요소의 값이 0인 배열 100개를 1차원으로 생성하기
f = np.zeros(100)
f.shape


#1 값  setting
# 모든 요소의 값이 1인 배열 100개를 1차원으로 생성하기
g = np.ones(100)
g.shape
#1으로 초기화된 10행 10열 배열 h생성하기
h =np.ones((10,10))
h
h.shape


#0~2까지의 숫자를 9개로 균등분할하여 배열 생성
j=np.linspace(0,2,9)
j
j.size
#0~9까지의 숫자를 20개로 균등분할한 배열 생성
k=np.linspace(0,9,20)
k
k.size

# numpy 데이터 연산
#1차원 배열의 연산
a = np.array([20,30,40,50])
b = np.arange(4) #([0,1,2,3])
c = a-b  #각각의 요소들을 연산
c # array([20, 29, 38, 47])
c = a+b  #각각의 요소들을 연산
c # array([20, 31, 42, 53])
c = a*b  #각각의 요소들을 연산
c # array([ 0,  30,  80, 150])



c = b**2 #b 요소들 각각의 제곱
c

c = a < 35 # a배열의 요소을 35와 비교하여 작으면 True,크면 False
c

#2차원 배열의 연산
'''
  a    @   b  =    c 
행 [1,1] [2,0]   [1*2+1*3][1*0+1*4]  [5,4]
   [0,1] [3,4]   [0*2+1*3][0*3+1*4]  [3,4]
'''
a=np.array([[1,1],[0,1]])
b=np.array([[2,0],[3,4]])
# @: 행렬의 곱. dot
c = a @ b
c
c = a.dot(b)
c

### 난수를 이용한 배열 생성
rg = np.random.default_rng(1) #seed값 설정
rg
a = rg.random((2,3)) #2행3열배열. 
a
b=np.ones((2,3),dtype=int)
b
a.dtype
b.dtype
c = a+b #실수형 = 실수형+정수형
c = b+a #실수형 = 실수형+정수형
c

#난수를 이용하여 0~9사이의 정수값을 가진 임의의수를 3행4열
# 배열 생성
#np.floor: 작은 근사정수
#np.ceil : 큰 근사정수
np.random.random((3,4))  # 0 <=r < 1
np.random.random((3,4)) * 10 # 0 <= r < 10
h=np.floor(np.random.random((3,4)) * 10)
h
h.ndim
h.shape
#h배열을 1차원배열 h1 변경하기
h1=h.ravel() #h배열이 변경되지 않음
h1.ndim
h1.shape
#h배열을 6행2열 배열 h2 변경하기
h2=h.reshape(6,2) #h배열이 변경되지 않음.
h2.shape
h.shape
#h배열 자체를 6행2열의 배열로 변경하기
h.resize(6,2)  #원본 수정
h.shape  #(6,2)
h

#3행을 지정. 열을 자동 맞춤
h.reshape(3,-1) #-1을 지정하면 자동으로 맞춤.
h.reshape(4,-1).shape #-1을 지정하면 자동으로 맞춤.
h.reshape(-1,4).shape
np.eye(10,10) #단위 행렬

# 0~9사이의 정수형 난수값을 가진 2행2열 배열 생성
#randint: 정수형 난수 리턴. 
i=np.random.randint(10,size=(2,2))
i
j=np.random.randint(10,size=(2,2))
j
#2개의 배열을 합하기
np.vstack((i,j)) #행기준 합. 열의 갯수가 같아야 함
np.hstack((i,j)) #열기준 합. 행의 갯수가 같아야 함.

#배열 나누기
k = np.random.randint(10,size=(2,12))
k
np.hsplit(k,3) #3개로 열을 분리. 
np.vsplit(k,2) #2개로 행을 분리. 
k.shape

#k배열의 모든 요소값을 100으로 변경하기
#k=100. k변수에 100 정수값을 저장. k값은 배열이 아님.
k.shape
k[0,0]=100
k[0,:]=100
k[:]=100
k[:,:]=200
k
#0~19사이의 임의의 정수를 가진 5행 4열 배열 l을 생성하기
l = np.random.randint(20,size=(5,4))
l
l.max()
#각 행의 최대값들을 조회하기
l.max(axis=1)
#각 열의 최대값들을 조회하기
l.max(axis=0)

#각 행의 최대값의 인덱스들 조회하기
l.argmax(axis=1)
#각 열의 최대값의 인덱스들 조회하기
l.argmax(axis=0)

#각 행의 최소값의 인덱스들 조회하기
l.argmin(axis=1)
#각 열의 최소값의 인덱스들 조회하기
l.argmin(axis=0)

n=[1,2,0,4,0] #리스트
type(n)
np.nonzero(n) #요소의 값이 0이아닌 요소의 인덱스 리턴


#정규분포값을 가진 임의의 수 10000개를 가진 배열
#np.random.normal : 정규분포에 맞는 난수 발생 함수
# (0,1,10000) => (평균,표준편차,데이터갯수)
#                 평균이 0, 표준편차가 1인 난수들
o = np.random.normal(0,1,10000)
o
o.shape
o.mean()
o.std()

#choice 함수 : 값을 선택.
#    choice(값의범위,선택갯수,재선택여부)
#    choice(값의범위,선택갯수,확률)
#(10,5,replace=False)
# 10 : 0~ 9사이의 값
# 5 : 5개 선택
# replace=True|False : 중복가능|중복불가
q=np.random.choice(10,5,replace=True)
q
#1~45사이의 수를 중복없이 6개를 선택한 r배열 생성
r = np.random.choice(45,6,replace=False) + 1
r
#정렬
r.sort()
r
#0~3사이의 수를 중복없이 5개 선택.
#오류. 중복되어야 함
s=np.random.choice(4,5,replace=False)  #오류. 불가능선택
s=np.random.choice(4,5,replace=True)
s
#확률 적용 선택
#choice(값의범위,선택갯수,확률)
# p=[0.1,0.2,0.3,0.2,0.1,0.1] 
# p의 전체 합: 1 
p=[0.1,0.2,0.3,0.2,0.1,0.1] 
sum(p)
t=np.random.choice(6,100,p=[0.1,0.2,0.3,0.2,0.1,0.1])
t
type(t)
listt=list(t) # 리스트 <= 배열

# for
for i in range(6):
    print(i, listt.count(i))
#comprehension
[(x,listt.count(x)) for x in range(6)]

























