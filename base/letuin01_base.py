
##### 02 python 기본 문법
###02-01 프로그램밍 기본  

# shift + enter  
# 문장의 연결

# text1 = "안녕 하세요 \
#        렛유인 입니다 "
# print(text1)


#  파일 저장 ctl + s
#  여러줄 주석

'''
   여러줄 주석
   여러줄 주석은 나중에 문자열 표현에서도 사용됨. 
'''


###02-02 출력 / 문자열 
## print(출력값, 출력값) 
print('hello')
print("hello")
#여러개의 데이터 화면에 출력
print(10,20,30,40,50)
#문자열을 여러번 출력
print("abc"*3)
print('abc'*3)


#문자열+숫자 안됨.
print("학번:"+100) #오류발생
print("학번:",100)
print("학번:"+"100") #문자열간의 +연산은 가능함
print("학번:"+str(100)) #str() : 문자열로 변환
print("'안녕하세요' 라고 말했습니다.")
print('"안녕하세요" 라고 말했습니다.')


 
## print(출력값1, end='')
print(10,end="\t") 
print(20,end="\t")
print(30,end="\n") #end 속성값의 기본값 : \n.
#10,20,30 출력
print(10,end=",")
print(20,end=",")
print(30) 
 
# 들여쓰기 오류 
# print("문장의 처음에 공백이 있으면 오류") #오류 
### print( 문자열  % )
# 형식문자를 이용하여 출력하기 : 
#  %d(10진수정수)
#  %f(실수)
#  %s(문자열)
print("%d * %d = %d" % (2.0,3,6))  # 2 * 3 = 6
print("%f * %f = %f" % (2,3,6))    # 2.000000 * 3.000000 = 6.000000
print("%.2f * %.2f = %.2f" % (2,3,6)) # 2.00 * 3.00 = 6.00
# %x,%X : 16진수 표현
print("%X" % (255))  #FF
print("%x" % (255))  #ff
print("안녕 %s!, 나도  %s" % ("홍길동","김삿갓"))

###-------------------------------

#format 함수를 이용한 출력
#{0:5d} : 첫번째값을 정수형 5자리로 출력
#{1:5d} : 두번째값을 정수형 5자리로 출력
#{2:10.2f} : 세번째값을 실수형 10자리로 소수 2자리  출력
# ctl+/ 주석
print("{0:5d}{1:5d}{2:10.2f}".format(100,200,300))
print("{1:5d}{2:5d}{0:5d}".format(100,200,300))



# print(f'{변수1} {변수2} 직접 변수이름으로 출력
a=100
b=200
print(a,b) #100 200
print(f"{a}와 {b}를 프린트 하겠습니다 ") #100와 200를 프린트 하겠습니다 

 
### 특수 문자 (Escape character)
#\" 
print("\"안녕하세요\" 라고 말했습니다.")
print('\'안녕하세요\' 라고 말했습니다.')

# \n : new line
print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사")


print("""동해물과 백두산이 마르고 닳도록
 하느님이 보우하사 우리나라 만세
 무궁화 삼천리 화려강산""")


### 문자 슬라이싱  
#문자열 : 문자들의 모임. 문자여러개. 문자의 배열로 인식
print("안녕하세요"[0]) #안
print("안녕하세요"[2]) #하 
###-----------------------
#문자열의 범위를 지정하여 출력하기
#문자열[첫번째인덱스:마지막인덱스+1:증감값]
print("안녕하세요"[0:2]) #안녕. 0번인덱스부터 1번인덱스까지
print("안녕하세요"[:2]) #안녕.  처음부터 1번인덱스까지
# 처음부터 4번인덱스까지 2칸씩
print("안녕하세요"[:5:2]) #안하요. 
print("안녕하세요"[2:]) #하세요. 2번인덱스 이후 
print("안녕하세요"[::2])#안하요
print("안녕하세요"[::-1])# 뒤부터   요세하녕안  
 
##### 문자열 함수 
'''
  len(문자열) : 문자열의 길이
  문자열.count(문자) : 문자열에서 문자의 갯수 리턴
  문자열.find(문자) : 문자열에서 문자의 위치 리턴
                     문자가 없는 경우 -1 리턴
  문자열.index(문자) : 문자열에서 문자의 위치 리턴
                     문자가 없는 경우 오류 발생
'''
###--- 문자열 함수 
a = "hello"
#a 문자열에서 l문자의 갯수 출력하기
cnt = 0
#len(a) : a문자열의 길이 5
for i in range(len(a)) : # 0 ~ 4까지값
    if a[i] == 'l' :
        cnt += 1
print(a,"에서 l 문자의 갯수:",cnt)  #2
print(a,"에서 l 문자의 갯수:",a.count('l'))  #2
print(a,"에서 a 문자의 갯수:",a.count('a'))  #0

#a 문자열에서 l문자의 위치(인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l'))  #2
print(a,"에서 l 문자의 위치:",a.index('l')) #2

a
#a 문자열에서 3번인덱스 부터 l문자의 위치(인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l',3))  #3
print(a,"에서 l 문자의 위치:",a.index('l',3)) #3
#a 문자열에서 3번인덱스 부터 o문자의 위치(인덱스) 출력하기
print(a,"에서 o 문자의 위치:",a.find('o',3))  #4
print(a,"에서 o 문자의 위치:",a.index('o',3)) #4

#a 문자열에서 4번인덱스 부터 l문자의 위치(인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l',4))  #-1
print(a,"에서 l 문자의 위치:",a.index('l',4)) #오류


#a 문자열에서 a문자의 위치(인덱스) 출력하기
print(a,"에서 a 문자의 위치:",a.find('a'))  #-1
print(a,"에서 a 문자의 위치:",a.index('a')) #오류. 예외처리필요

#https://github.com/mskim3578/letuin_250204/tree/master

#문자열의 종류 알려주는 함수 한개의 ss를 실행후에 
# 아래 if문을 실행 한다 
ss = '123'
ss = 'Aa123'
ss = 'Aa'
ss = 'AA'
ss = 'aa'
ss = '     '
ss = '  aa   '
ss = '  Aa   '



if ss.isdigit() :
    print(ss,": 숫자")
if ss.isalpha() :
    print(ss,": 문자")
if ss.isalnum() :
    print(ss,": 문자 또는 숫자")
if ss.isupper() :
    print(ss,": 대문자")
if ss.islower() :
    print(ss,": 소문자")
if ss.isspace() :
    print(ss,": 공백")

#--------
ss = "홍길동"
if ss.startswith("(") == False :   # ss 문자열이 '('시작하지 않으면 '('추가하기   
     ss='('+ss

if ss.endswith(")") == False : # ')' 끝나지 않으면  ')' 추가하기
    ss = ss + ')'

print(ss)


########## 3. 변수

#### 자료형 : 변수선언하지 않고 사용
# 변수의 자료형은 값으로 결정됨.
n = 10
type(n)
n = 10.5
type(n)
n='안녕'
type(n)
len(n)
### 주의 사항 !!!!!!   예약어를 변수로 잡으면 예약어의 기능이 없어진다 
#값이  
len=9  # len()함수가 int 타입으로 변경됨 아래의 내용이 error 난다 
del len # 해야한다 
#len() : 문자열의 길이
print(len("안녕하세요"))
len("안녕하세요") 

#### 4.  기본함수  :  


#자연수를 입력받아 +100을한 값을 출력하기
num = int(input("자연수를 입력하세요"))
num += 100
print(num)
# 형변환 함수
# int() : 정수형으로 변환
# float() : 실수형으로 변환
# str() : 문자열형으로 변환
print("num+100="+str(num))
print("num+100=",num)
###---------------------------
#2,8,16 진수를 10진수로 변환
#문자를 숫자 진수 표현식식
print(int("11",2))
print(int("11",8))
print(int("11",16))
#10진수를 2,8,16진수로 변환
print(10,"의 2진수:",bin(10))
print(10,"의 8진수:",oct(10))
print(10,"의 16진수:",hex(10))

#### 5. 연산자 

# 산술연산자 : +,-,* , /, %, // ,**
5+7
5*7
5/7
7%5
5%7
5//7  #정수형 몫의 값
5**2  # 5*5. 제곱
5^2  # 비트연산자 (XOR)
   
#대입연산자 : =, +=, -=, *=,....
a=10
a += 10
a    
a -=5
a    
a *=2    
a

    
# 키보드에서 초를 입력받아 몇시간 몇분 몇초인지 출력하기
# input함수:키보드에서 입력받기.
#           문자열형태로 입력받음.


second = int(input("초를 입력하세요:"))
print(second//3600,"시간",(second%3600)//60,"분",\
      (second%60),"초")
 
 
 
# 연습문제 2 : 
# 금액(3650)을 입력 받아 잔돈(500,100,50,1)으로 바꿔주는 프로그램을 작성 하기 
# input함수:키보드에서 입력받기.
#           문자열형태로 입력받음.


money = int(input("금액을 입력하세요:"))
print("500원 동전의 갯수", money//500) 
print("100원 동전의 갯수", money%500//100)
print("50원 동전의 갯수", money%100//50)
print("10원 동전의 갯수", money%50//10)
print("1원 동전의 갯수", money%10)



### 조건문 : if문
# 들여쓰기 해야함

score = 65
if score >= 90 :
    print("A학점")
    print("합격입니다.")
else : 
    if score >= 80 :
        print("B학점")
        print("합격입니다.")
    else :
       if score >= 70 :
         print("C학점")
         print("합격입니다.")
       else :
        if score >= 60 :
               print("D학점")
        else :
            print("F학점")
            
            
            
# if elif 구문
if score >= 90 :
   print("A학점")                
   print("합격입니다.")
elif score >= 80 :
   print("B학점")                
   print("합격입니다.")
elif score >= 70 :
    print("B학점")                
    print("합격입니다.")
elif score >= 60 :
   print("D학점")                
   print("합격입니다.")
else :
   print("F학점")                
   print("불합격입니다.")     


score = 70    
if(score >= 60) :
   print("합격입니다.")
   print("자격증을 받으러 오세요")   
   
   

# 간단한 조건식
# TRUE if 조건식 else FALSE
score = 65
print(score,"점수는",'PASS' if score>=60 else 'FAIL')       
    



    
# 반복문
#1부터 100까지의 합 구하기
num = 100
hap = 0
# range(1,num+1,증감값) : 1 ~ num까지의 숫자들
for i in range(1,num+1) :
    hap += i
print ("1부터 %d까지의 합:%d" % (num,hap))   


#1 ~ 100 까지 짝수의 합 구하기

hap=0
for i in range(1,num+1) :
    if i % 2== 0 :
       hap += i
print ("1부터 %d까지의 짝수합:%d" % (num,hap))   


hap=0
for i in range(2,num+1,2) :
    hap += i
print ("1부터 %d까지의 짝수합:%d" % (num,hap))   

#12345 반복문을 이용하여 출력하기
print(12345)

for i in range(1,6) :
    print(i,end="")


# while 조건문: 조건문의 결과가 참인 동안 반복함
num = 1
while num <= 5 :
  print(num, end="")
  num += 1      

#break : 반복문 종료
#continue : 반복문의 처음으로 제어 이동
hap = 0
for i in range(1,11) : #1 ~ 10
   if i == 5 :
       break;
   hap += i
print('hap=',hap) # 10   


hap = 0
for i in range(1,11) :
   if i == 5 :
       continue
   hap += i
print('hap=',hap)  # 50  


###-----
#중첩반복문 (구구단)
i,j=0,0  #초기화 방식
for i in range(2,10) :  # 2 ~ 9
    print("%5d단" % i)
    for j in range(2,10) : # 2 ~ 9
        print("%2d X %2d = %3d" % (i,j,(i*j)))
    print()   


###---
'''
1. 직각 삼각형 출력하기

*
**
***
****
*****

'''

h=5
### 1 ####
for i in range(1,h+1) :
   for j in range(1,i+1) :
       print("*",end="")
   print()    

### 2 ####
for i in range(1,h+1) :
   print("*"*i)   

###-----
'''
2. 역 직각 삼각형 출력하기

*****
****
***
**
*
'''
for i in range(h,0,-1) :
   for j in range(1,i+1) :
       print("*",end="")
   print()    

for i in range(h,0,-1) :
   print("*"*i)

