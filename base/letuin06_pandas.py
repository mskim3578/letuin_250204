import pandas as pd
# pip install pandas
import seaborn as sns #시각화모듈
# pip install seaborn   #cmd

#튜플 데이터를 Series 데이터로
tuple_data = ("홍길동",'1991-01-25','남',True)
sr = pd.Series(tuple_data)
sr = pd.Series(tuple_data,index=["이름","생년월일","성별","학생여부"])
print(sr.head(10))
print(sr.info())
print(sr.index) #값의 이름
print(sr.values)

sr = pd.Series(tuple_data)
print(sr.info())
print(sr.index) #값의 이름
print(sr.values)


#리스트를 Series로 만들기
list_data = ["홍길동",'1991-01-25','남',True]
sr = pd.Series(list_data,index=["이름","생년월일","성별","학생여부"])
print(sr)
print(sr.index) #값의 이름
print(sr.values)

#Series 조회

#한개의 값만 조회
print(sr[0])  #순서로 조회.
print(sr["이름"]) #인덱스로 조회
print(sr.이름) #인덱스로 조회A
print(sr[1])  #순서로 조회.
print(sr["생년월일"]) #인덱스로 조회A
print(sr.생년월일) #인덱스로 조회


#여러개의 값 조회 : list, 구간 0:10
print(sr[[0,1]])  #순서로 조회
print(sr[['이름','생년월일']])  #인덱스 조회
#print(sr['이름','생년월일'])  #오류발생
#여러개의 값 조회. 범위 지정하여 조회
print(sr[0:2])  #순서로 조회. 마지막값 앞까지
print(sr['이름':'성별'])  #인덱스 조회. 마지막 값 까지




#리스트를 이용하여 데이터프레임 객체 생성
df = pd.DataFrame([[15,'남','서울중'],[17,'여','서울여고'],
                   [17,'남','서울고']])
df

###------- 데이터 프레임 객체 생성하기





df = pd.DataFrame([[15,'남','서울중'],[17,'여','서울여고'],
                   [17,'남','서울고']],
                  index=['홍길동','성춘향','이몽룡'],
                  columns=['나이','성별','학교'])    
print(df)
print(df.index)
print(df.columns)
print(df.head())


# 딕셔너리 이용 (key:columns)
dict_data= {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],
            'c3':[10,11,12],'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(df)
print("컬럼명:",df.columns) #열의이름
print("인덱스명:",df.index) #행의이름 


#rename : 컬럼명,인덱스명의 일부만 변경하기
# inplace=True : 객체 자체 변경
# rename에서 변경 자료는 dictionary임
df.rename(columns={"age":"나이"},inplace=True)   #default    inplace=False
print(df)



#inplace=True 사용하지 않으면, df= 대입구문이 대체 효과.
df.rename(index={"학생1":"홍길동"})  #inplace=True 효과
print(df)
df = df.rename(index={"학생1":"홍길동"})  #inplace=True 효과
print(df)

###  통계정보 
exam_data={'수학':[90,80,70],'영어':[98,88,95],
           '음악':[85,95,100],'체육':[100,90,90]}
#1
df=pd.DataFrame(exam_data, index=['홍길동','이몽룡','김삿갓'])
print(df)
#2
df=pd.DataFrame(exam_data)
df.index=['홍길동','이몽룡','김삿갓']
print(df)
#mean() : 평균    column기준으로 row(index)의 평균 :  column값의 평균임
print(df.mean())
print(type(df.mean()))  #serise
#수학평균
print('수학평균', df.mean()['수학'])
print('수학평균', df['수학'].mean())
print(df['수학'])

#수학총점
print(df.sum())  #columns  합산
print('수학총점', df.sum()['수학'])
print('수학총점', df['수학'].sum())

#과목별 최대점수
print(df.max())
print('최대점수', df.max()['수학'])
print('최대점수', df['수학'].max())

#수학의 중간값
print(df.median()["수학"])
print(df["수학"].median())
#   데이터의 갯수 홀수 : 가운데 값.
#   데이터의 갯수 짝수 : 가운데 두값의 평균.

###-----
#표준편차 : std() : sqrt((평균값-값) ** 2 합계)
#                  sqrt(분산)
# 분산 : var() 
# 분산 : 편차의 평균이고 
# 표준편차는  sqrt(분산)

df.std() #표준편차
df.var() #분산

#기술통계 => 기본적인 수치데이터조회 
test=df.describe()
type(df.describe())
type(test)
test.info()
'''         수학         영어          음악          체육
count   3.0   3.000000    3.000000    3.000000
mean   80.0  93.666667   93.333333   93.333333
std    10.0   5.131601    7.637626    5.773503
min    70.0  88.000000   85.000000   90.000000
25%    75.0  91.500000   90.000000   90.000000
50%    80.0  95.000000   95.000000   90.000000
75%    85.0  96.500000   97.500000   95.000000
max    90.0  98.000000  100.000000  100.000000

<class 'pandas.core.frame.DataFrame'>
Index: 8 entries, count to max
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   수학      8 non-null      float64
 1   영어      8 non-null      float64
 2   음악      8 non-null      float64
 3   체육      8 non-null      float64
dtypes: float64(4)
memory usage: 320.0+ bytes

'''

#수학 통계정보
df.describe()["수학"]
df["수학"].describe()
#간략정보
df.info()
df["수학"].info()  
#데이터의 처음 일부(5개) 조회
df.head()
#데이터의 마지막 5개 조회
df.tail()

#홍길동 데이터 조회하기
print(df.수학)
print(df["수학"])
#인덱스명으로 조회하기 => 행을 값 조회. .loc 사용
# loc[인덱스명] : 인덱스에 해당하는 행을 조회
# iloc[순서] : 순서 해당하는 행을 조회

print(df.loc["홍길동"]) #홍길동 행(index) 조회
print(df.iloc[0])  #첫번째 행 조회
type(df.loc["홍길동"])  #Series 객체
print(df.loc["홍길동"].mean())
print(df.loc["홍길동"].median())
print(df.loc["홍길동"].describe())
print(type(df.loc["홍길동"].describe()))

###--------
#drop() : 행,열 제거하기
#axis=0 : 행을 의미 (index)
#axis=1 : 열을 의미 (column)
#행 제거하기

df1=df.copy()
#행 제거하기
df1.drop(["홍길동"], axis=0, inplace=True)
#열 제거하기
df1.drop(["체육"], axis=1, inplace=True)

#열 제거 
del df1["음악"]
df1


###---------------------------------
#df 데이터의 이몽룡(row, index) 학생 점수 조회하기

df.iloc[1] #순서 조회
df.loc[["이몽룡","김삿갓"]] #인덱스이름
df.iloc[[1,2]] #순서 조회
df.iloc[1:2] #순서 조회

#범위로 조회하기
df.loc["이몽룡":"김삿갓"] #이몽룡부터 김삿갓까지 
df.loc["이몽룡":] #이몽룡부터 끝까지 
df.loc[:"이몽룡"] #처음부터 이몽룡까지 
df.loc[:] #처음부터 끝까지 

#처음부터 끝까지 2칸씩 조회
df.loc[::2] 
#처음부터 끝까지 역순으로 조회
df.loc[::-1]

# 1번부터 2번까지 
df.iloc[1:3]  
#1번부터 끝까지 
df.iloc[1:]
#처음부터 1번까지 
df.iloc[:2]
df.iloc[:] #처음부터 끝까지 
df.iloc[::2] #처음부터 끝까지 2칸씩 조회
df.iloc[::-1] #처음부터 끝까지 역순으로 조회 

exam_data={"이름":["서준","우현","인아"],
           "수학":[90,80,70],
           "영어":[98,89,95],
           "음악":[85,95,100],
           "체육":[100,90,90]}
df=pd.DataFrame(exam_data)
df
#1. 총점 컬럼을 추가한다 
df["총점"]=df["수학"]+df["영어"]+df["음악"]+df["체육"]
'''
 이름  수학  영어   음악   체육   총점
0  서준  90  98   85  100  373
1  우현  80  89   95   90  354
2  인아  70  95  100   90  355
'''
#2. 이름 컬럼을 인덱스 설정하기
df.set_index("이름",inplace=True)  #이름 컬럼을 인덱스로 수정
df

#3. 이름의 역순으로 정렬하기
df.sort_index(ascending=False,inplace=True)
df

#4. 과목별 역순으로 정렬하기
df.info()
df.sort_values(by="영어",ascending=False,inplace=True)
df
df.sort_values(by="음악",ascending=False,inplace=True)
df
df.sort_values(by="총점",ascending=False,inplace=True)
df

#5. 조건에 대한 분류 df[조건식]
df[df['총점'] >= 355]

# pandas test source
#read_csv : jeju1.csv 파일 읽어 DataFrame 객체로 생성
df=pd.read_csv("data/jeju1.csv")
+type(df)
df.info() #간략 정보
df.head() #상위 5건조회
df.tail() #하위 5건조회
df
# 장소만 조회  
df.장소
df['장소'] # serise
df[['장소']]
type(df[['장소']])

# LON, LAT 조회  
df[['LON', 'LAT']]
df.index
#set_index : 장소  컬럼을 인덱스로 변경하기
df.set_index('장소', inplace=True)
df
df.info()
'''
               LON        LAT
장소
제주국제공항       126.496217  33.505314
돔베돈          126.526687  33.516084
공룡랜드         126.433153  33.442382
협재해수욕장       126.240463  33.404218
한림공원         126.239262  33.390101
유리의성         126.273744  33.315127
오설록티뮤지엄      126.289451  33.306537
테디베어뮤지엄      126.408691  33.267972
저녁_오성식당      126.414549  33.256059
중문관광단지       126.412361  33.249186
숙소_서귀포KAL호텔  126.580954  33.248020
'''
df.loc["돔베돈"]
df.loc[["돔베돈"]]
df.index
#인덱스 값을 여행지 컬럼으로 추가하기
#컬럼추가:dataframe[새로운컬럼명]=값
#컬럼수정:dataframe[기존컬럼명]=값
df['여행지']=df.index
df.info()

#현재의 index값을 컬럼으로 변경하기
df.reset_index(inplace=True)
df.info()
df
df.index

#장소 컬럼 제거하기
df.drop("장소",axis=1,inplace=True)
df
# df데이터의 내용을 csv 파일로 저장하기
# to_csv("파일이름",index=False)
# index=False : 인덱스는 파일에 저장 안함
#               기본값 True
df.to_csv("data/df_jeju1.csv",index=False) #index 제외
df.to_csv("data/df_jeju2.csv")  #index 포함


#excel 파일 읽기
'''
read_excel("파일이름","sheet이름","인덱스컬럼")
'''


df = pd.read_excel("data/sales_2015.xlsx",sheet_name=None,index_col=None)
df
type(df) #딕셔너리 객체 데이터 
'''
  {"sheet이름":dataframe 데이터,...}
'''
df_all=pd.DataFrame([])
for name, data   in df.items() :
    # print("sheet name", name)
    # print("data 자료형", type(data))
    df_all = pd.concat([df_all, data], axis=0) #row(index) 합친다 

df_all.info()
df_all.Amount
df_all.columns= ['ID', 'Name', 'Invoice','Amount','Date'] 

#['Customer ID', 'Customer Name', 'Invoice Number', 'Sale Amount',"Purchase Date']

##### 조건에 의한 조회
#Sale Amount 컬럼의 값이 500보다 큰 레코드만 조회
# 조건에 해당하는 index:row를 프린트 한다 
df_500=df_all[df_all["Amount"] > 500]
df_all.loc[df_all["Amount"] > 500]

#매입일자가 2015-03-17일 정보만 조회하기
df_all[df_all["Date"] == '2015-03-17']
df_0317 = df_all[df_all["Date"] == '2015-03-17']
df_0317


#df500데이터를 pd_sale_2015.xlsx 파일의
# 2015_500 sheet로 저장하기

#내용 없는 파일
outexcel = pd.ExcelWriter("data/pd_sale_2015.xlsx")
# 전체파일에 sheet를 추가 하여 저장 한다 
df_500.to_excel(outexcel, sheet_name="2015_500", index=False)
df_all.to_excel(outexcel, sheet_name="2015", index=False)
df_0317.to_excel(outexcel, sheet_name="0317", index=False)
outexcel._save()    #save() 에서 수정 되었


##################################################
# titanic 데이터셋 연습(데이터 전처리)
# seaborn 모듈에 저장된 데이터
'''
survived	생존여부
pclass	좌석등급 (숫자)
sex	성별 (male, female)
age	나이
sibsp	형제자매 + 배우자 인원수
parch: 	부모 + 자식 인원수
fare: 	요금
embarked	탑승 항구
class	좌석등급 (영문)
who	성별 (man, woman)
adult_male 성인남자여부 
deck	선실 고유 번호 가장 앞자리 알파벳
embark_town	탑승 항구 (영문)
alive	생존여부 (영문)
alone	혼자인지 여부
'''

#seaborn 모듈에 저장된 데이터셋 목록
print(sns.get_dataset_names())
#titanic데이터 로드. 
titanic = sns.load_dataset("titanic")
titanic.info()
#
titanic.head(10)
titanic
#pclass,class 데이터만 조회하기
titanic[["pclass","class"]].head()

#컬럼별 건수 조회하기
titanic.count() #결측값을 제외한 데이터
# 건수 중 가장 작은 값 조회하기
titanic.count().min()
# 건수 중 가장 작은 값의 인덱스 조회하기
titanic.count().idxmin()  #deck
type(titanic.count())

#titanic의 age,fare 컬럼만을 t_df 데이터셋에 저장하기
t_df=titanic[['age','fare']]
t_df.info()

#df 데이터의 평균 데이터 조회
t_df.mean()
#df 데이터의 최대나이와 최소나이 조회
t_df.age.max()
t_df.age.min()
#나이별 인원수를 조회. 최대 인원수를 가진 5개의 나이 조회

#값의 갯수. 내림차순 정렬하여 조회 
t_df.age.value_counts()
t_df.age.value_counts().head()

#인원수가 많은 나이 10개 조회 
t_df.age.value_counts().head(10)










    