import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
plt.rc("font",family="Malgun Gothic")


#  data/chipotle.tsv    read
chipo = pd.read_csv("data/chipotle.tsv",sep="\t")
chipo.info()
chipo.head()
'''
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   order_id            4622 non-null   int64
 1   quantity            4622 non-null   int64
 2   item_name           4622 non-null   object
 3   choice_description  3376 non-null   object
 4   item_price          4622 non-null   object
dtypes: int64(2), object(3)
memory usage: 180.7+ KB
'''

#chipo 데이터의 행열의 갯수 출력하기
chipo.shape  # (4622,5)
#컬럼명
chipo.columns
#인덱스명
chipo.index
# order_id 주문번호이므로, 숫자형 분석의 의미가 없다.
# order_id  컬럼의 자료형을 문자열로 변경하기
chipo["order_id"] = chipo['order_id'].astype(str)
chipo.info()

#판매상품명과 상품의 갯수 출력하기
chipo['item_name'].unique()
len(chipo['item_name'].unique())

#item_price 컬럼을 실수형 변경
chipo.head()
chipo['item_price']=chipo['item_price'].str.replace('$','').astype(float)
chipo.info()

#######   groupby  ====
#ex01)주문금액 합계
hap=chipo['item_price'].sum() # 34500.16
#ex02) 주문건수
cnt=len(chipo['order_id'].unique())   #1834
len(chipo.groupby('order_id'))

# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001DC8F2E3920>
#ex03) 주문당평균금액
hap/cnt   # 18,81~
chipo.groupby('order_id')['item_price'].sum().mean()

#ex04) 50달러 이상 주문한 주문번호
chipo.groupby('order_id').sum()
'''
          quantity  ... item_price
order_id            ...
1                4  ...      11.56
10               2  ...      13.20
100              2  ...      10.08
'''
order_id_tot = chipo.groupby('order_id')['item_price'].sum()
# 
# 50달러 이상 
result = order_id_tot[order_id_tot>=50]
len(result.index)  #28

#ex05) 50달러 이상 주문한 주문정보
chipo_50 = chipo[chipo['order_id'].isin(result.index)]
chipo_51 = chipo.groupby('order_id')\
           .filter( lambda x : sum(x['item_price']) >= 50)
chipo_50.info()
chipo_51.info()

#ex06) item_name 별 단가를 조회하기
price_one=chipo.groupby('item_name')
price_one
len(price_one) #50
len(chipo['item_name'].unique())

for key, item in price_one:
    print(key, "=", len(item), item['item_price'].min())
    #print(item['item_price'].min())
price_min = chipo.groupby('item_name')['item_price'].min()
price_min = chipo.groupby('item_name').min()['item_price']

    
#ex07) 단가의 분포를 히스토그램으로 출력하기    
  
plt.rc("font", family="Malgun Gothic")
plt.hist(price_min)
plt.ylabel("상품갯수")
plt.title("상품단가 분포")

#price_min.plot(kind = "hist")
plt.ylabel("상품갯수")
plt.title("상품단가 분포")
plt.show()

#ex08) 주문당 금액이 가장 높은 5건의 주문 총수량을 조회하기

price5 = chipo.groupby('order_id').sum()\
        .sort_values(by='item_price', ascending=False)[:5]
type(price5.index)
price5.index
    
#ex09) 주문당 금액이 가장 높은 5건의 주문 정보 조회하기 
chipo_5 = chipo[chipo["order_id"].isin(price5.index)]  
chipo_5.info()  #66
    
#ex10) Chicken Bowl 몇번 주문되었는지 출력하기
chipo_chicken = chipo[chipo['item_name']=='Chicken Bowl']
len(chipo_chicken) #726
len(chipo_chicken.groupby('order_id'))  #615

###################
#  전세계 음주 데이터 분석하기 : drinks.csv
import pandas as pd
drinks = pd.read_csv("data/drinks.csv")
drinks.info()
'''
  country : 국가명
  beer_servings : 맥주소비량
  spirit_servings : 음료소비량
  wine_servings : 와인소비량   
  total_litres_of_pure_alcohol : 순수 알콜량
  continent : 대륙명
'''
drinks.head()
# 변수 = 컬럼 = 피처
# 상관계수 : 두연속적인 데이터의 상관관계 수치
# 피어슨 상관계수 : 기본. 
beer_wine_corr=\
    drinks[["beer_servings","wine_servings", "spirit_servings"]].corr()
beer_wine_corr
'''
               beer_servings  wine_servings
beer_servings       1.000000       0.527172
wine_servings       0.527172       1.000000

'''
import seaborn as sns

sns.heatmap(beer_wine_corr, annot=True, cmap='coolwarm')
plt.title("beer_wine_corr")
plt.show()


drinks.columns 
cols = drinks.columns[1:-1]
cols
corr = drinks[cols].corr()
corr
corr.values

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("columns")
plt.show()
#seaborn 모듈의 산점도을 이용하여 시각화 하기
sns.pairplot(drinks[cols])
plt.show()

#회귀그래프 작성하기
sns.regplot\
 (x="beer_servings",y="total_litres_of_pure_alcohol",
  data=drinks)
plt.show()

#각 변수의 결측값 갯수 조회하기
drinks.info()
drinks.isnull().sum()


drinks["continent"].value_counts()  #각 value별 합계
drinks["continent"].value_counts(dropna=False)  #null 포함
#대륙별 국가수 조회하기
drinks.groupby("continent").count()["country"]
#continent 컬럼의 결측값을 OT로 변경하기
#fillna : 결측값을 다른 값으로 치환함수
drinks["continent"]=drinks["continent"].fillna("OT")
drinks.info()
labels=drinks["continent"].unique()
explode=[0.1,0,0,0.1,0,0]
plt.pie(drinks["continent"].value_counts(),
       labels=labels,
       autopct='%.0f%%',
       explode=explode,
       shadow=True)
plt.title('null data to \'OT\'')
plt.show()
drinks.info()



drinks["continent"]=drinks["continent"].fillna("OT")
drinks.info()

# 1 대륙별 total_litres_of_pure_alcohol 섭취량 평균
drinks['continent']=drinks['continent'].astype(str)
cont_mean=drinks.groupby("continent")['total_litres_of_pure_alcohol'].mean()
# cont_mean=drinks.groupby("continent").mean()['total_litres_of_pure_alcohol'] #error contry object 
# 알콜 섭취량의 평균
total_mean=drinks["total_litres_of_pure_alcohol"].mean()

# 2 대륙명 : x축의 라벨
continents = drinks['continent'].unique().tolist() # nparray는 tolist() 만 가능 하다 
continents.append('Mean')
len(continents)
#  y축의 라벨
len(cont_mean)
alcohol= cont_mean.tolist()  # serise는 tolist(), to_list() 가능 
len(alcohol) #6

#y축 데이터 : 대륙별 평균값
alcohol.append(total_mean)
len(alcohol) # y : 7
'''
[3.0075471698113208, 2.1704545454545454, 8.617777777777778, 3.38125, 5.995652173913044, 6.308333333333334, 4.717098445595855]
'''
x_pos = np.arange(len(continents))
bar_list=plt.bar(x_pos, alcohol, align='center', alpha=0.5)
bar_list[len(continents) - 1].set_color('r')
plt.xticks(x_pos, continents)
plt.ylabel('total_litres_of_pure_alcohol') #y축설명
plt.title('대륙별 '+'total_litres_of_pure_alcohol'+' 섭취랑') #제목   
plt.show()


####   continent별 수량 column별 chart
drinks["continent"]=drinks["continent"].fillna("OT")
drinks.info()


def bar_chart(colname):
    print(colname)
    cont_mean=drinks.groupby("continent")[colname].mean()
    total_mean=drinks[colname].mean()
    continents = drinks['continent'].unique().tolist() 
    continents.append('Mean')
    len(continents) #7
    len(cont_mean)
    alcohol= cont_mean.tolist()  # serise는 tolist(), to_list() 가능 
    len(alcohol) 
    alcohol.append(total_mean)
    len(alcohol) #7
    x_pos = np.arange(len(continents))
    bar_list=plt.bar(x_pos, alcohol, align='center', alpha=0.5)
    bar_list[len(continents) - 1].set_color('r')
    plt.xticks(x_pos, continents)
    plt.ylabel('total_litres_of_pure_alcohol') #y축설명
    plt.title('대륙별 '+colname+' 섭취랑') #제목   
    plt.show()
col = drinks.columns.to_list()[1:-1]
bar_chart(col[0])
drinks.info()

#####  대한민국은 얼마나 술을 독하게 마시는 나라인가?
drinks = pd.read_csv("data/drinks.csv")
drinks.info()

#total_servings : 전체 주류 소비량 컬럼 추가
drinks["total_servings"] =\
    drinks["beer_servings"] + \
    drinks["spirit_servings"] +\
    drinks["wine_servings"]
    
drinks["alcohol_rate"] = \
    drinks["total_litres_of_pure_alcohol"]/drinks["total_servings"]
#1. alcohol_rate null인 index 구하기
#alcohol_rate 컬럼에 결측값 존재.
#전체주류소비량이 0인 경우 불능 => 결측값
#alcohol_rate 컬럼의 값이 결측값인 레코드 조회하기
alcoholnull = drinks[drinks["alcohol_rate"].isnull()]
len(alcoholnull)
#2. alcohol_rate 컬럼의 결측값을 0을 치환하기
drinks["alcohol_rate"]=drinks["alcohol_rate"].fillna(0)
drinks.info()

#alcohol_rate의 값으로 내림차순 정렬하기. alcohol_rate_rank 저장
alcohol_rate_rank=drinks.sort_values(by="alcohol_rate", ascending=False)\
                [["country","alcohol_rate"]]

alcohol_rate_rank


alcohol_rate_rank.head()
alcohol_rate_rank.shape #(193,2)

alcohol_rate_rank.country.tolist().index("South Korea") #14

#국가명목록
country_list = alcohol_rate_rank.country.tolist()

#1. x축값
x_pos = np.arange(len(country_list))
#2. y축값
rank=alcohol_rate_rank.alcohol_rate.tolist()
#막대그래프 
# bar_list : 막대 목록
bar_list = plt.bar(x_pos, rank)
#대한민국 막대의 색을 red로 변경
korea_rank = country_list.index("South Korea")
bar_list[korea_rank].set_color('r')
plt.ylabel('alcohol rate')
plt.title('liquor drink rank by contry')

#korea_serving_rate : 대한민국 전체 술소비량 데이터. y축값

korea_alcohol_rate = alcohol_rate_rank[ alcohol_rate_rank['country']=='South Korea']['alcohol_rate'].values[0]
korea_alcohol_rate     #0.0593939393939394


plt.annotate('South Korea : ' + str(korea_rank + 1)+"번째", #text
          xy=(korea_rank, korea_alcohol_rate), #좌표
          xytext=(korea_rank + 10, korea_alcohol_rate+0.1 ), #text 위치 
          arrowprops=dict(facecolor='red', shrink=0.05)) 


plt.show()
