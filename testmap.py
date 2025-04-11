
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
###############
#  지도 시각화
#  html 보기  파일명 ->우클릭 -> Open externally
import folium   #pip install folium
#location=[37.55,126.98] : 지도의 중앙 GPS값
#zoom_start=12 : 지도 확대값 
seoul_map = folium.Map(location=[37.55,126.98],zoom_start=12)
seoul_map.save("html/seoul.html")  #html 파일 생성.
'''
않되는것이 있음
seoul_map2 = folium.Map(location=[37.55,126.98],zoom_start=12,
                        tiles="stamenwatercolor")
seoul_map2.save("html/seoul2.html")  #html 파일 생성.
'''
'''
tiles : 지도 표시되는 형식 설정.
     openstreetmap : 기본값
     cartodbdark_matter
     cartodbpositron
     cartodbpositrononlylabels
     stamentonerbackground
     stamentonerlabels
   #  stamenterrain, Stamen Terrain
   #  stamenwatercolor
     stamentoner, Stamen Toner
'''
#index_col=0 : 첫번째 컬럼을 index로 설정
df = pd.read_excel("data/서울지역 대학교 위치.xlsx",index_col=0)
df.info()

seoul_map = folium.Map(location=[37.55,126.98],zoom_start=12)
'''
folium.Marker : 지도에 마커 표시객체.
  [lat,lng] : 위도 경도. 마커가 표시될 위치
  popup=name : 마커 클릭시 표시되는 내용
  tooltip=name : 마커ㅓ 내부에 마우스커서가 들어온 경우 표시되는 내용
  
add_to(seoul_map) : seoul_map 지도에 추가  

zip : 목록을 하나씩 연결하여 튜플객체의 리스트로 생성 
'''   
df.head()
for name,lat,lng in zip(df.index,df.위도,df.경도) :
    #name:대학교명
    #lat : 위도
    #lng : 경도
   folium.Marker\
       ([lat,lng],popup=name,tooltip=name).add_to(seoul_map)
seoul_map.save("html/seoul3.html")

