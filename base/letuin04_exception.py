   
#mystr 문자열에 파이썬 문자의 위치를 strpos 리스트에 저장하기
mystr = "파이썬 공부 중입니다. 파이썬을 열심히 공부합시다"

#1 find를 이용한 문자 찾기
strpos = []
index=0
while True :
    index = mystr.find("파이썬",index) #index 이후부터 검색 
    if index < 0: #없다
        break
    strpos.append(index)  #0,13
    index += 1            #14
print(strpos)      #[0, 13]



#2 index 함수 사용. 예외처리
strpos = []
index=0
while True :
  try :
    index = mystr.index("파이썬",index)
    strpos.append(index)  #0,13
    index += 1            #14
  except :  #오류 발생시 호출되는 영역
    break  
print(strpos)    


#다중예외처리 : 하나의 try 구문에 여러개의 except 구문이 존재
#              예외별로 다른 처리 가능
num1 = 1
num2 = "A"
try :
    n1 = int(num1)
    n2 = int(num2)
    print(n1+n2)
    print(n1/n2)
except ValueError as e:
    print("숫자로 변환 불가")
    print(e)
except ZeroDivisionError as e :
    print("두번째 숫자는 0안됨")
    print(e)
finally :  #정상,예외 모두 실행되는 구문
    print("프로그램 종료")   


# 다중 예외를 하나로 묶기
num1 = 1
num2 = "A"
try :
    n1 = int(num1)
    n2 = int(num2)
    print(n1+n2)
    print(n1/n2)
except (ValueError, ZeroDivisionError)  as e:
    print("입력 오류")
    print(e)

finally :  #정상,예외 모두 실행되는 구문
    print("프로그램 종료")   
    



#else 블럭 : 오류 발생이 안된경우 실행되는 블럭

try:
    age = int(input("나이를 입력하세요"))
except:
    print("숫자만 입력 하세요")
else:  #정상적인 경우 
    if age < 19 :
        print(age, ":미성년")
    else :
        print(age, ":성년")



        
# raise : 예외 강제 발생
try :
  print(1)    
  raise ValueError
  print(2)
except ValueError :
  print("ValueError 강제 발생")  
  
#pass 예약어 : 블럭 내부에 실행될 문장이 없는 경우
n=9
if n>10 :
    pass
else :
   print("n의 값은 10 이하입니다.")    
    
try :
    age = int(input("나이를 입력하세요"))
    if age < 19:
        print("미성년")
    else :
        print("성년")  
except ValueError :
    pass    #오류 발생시 무시.   

def dumy() :
    pass
  
  


