###------------함수 
#함수는 특정 작업을 수행하는 코드 블록이다 
#함수를 사용하면 코드를 재사용할 수 있고, 프로그램을 더 구조적으로 만들 수 있다

def func1() :
    print("func1() 함수 호출됨")
    return 10  #함수 종료 후 값을 리턴

def func2(num) :
    print("func2() 함수 호출됨:",num)
     #리턴값이 없는 함수

a=func1()      # func1() 함수 호출됨
print(a)       # 10
b=func2(100)   # func2() 함수 호출됨: 100
print(b)       #   None
func2('abc')   # func2() 함수 호출됨: abc


###-------지역변수, 전역변수
def func3() :
    c=300 #지역변수
    print("func3() 함수 호출:",a,b,c)
def func4() :
    a=110 #지역변수
    b=220 #지역변수
    print("func4() 함수 호출:",a,b)
#함수 내부에서 전역 변수값 수정하기
def func5() :
    global a,b   #a,b 변수는 전역변수를 사용함
    a=110
    b=220
    print("func5() 함수 호출:",a,b)

a=100
b=200

func3()                    # func3() 함수 호출: 100 200 300
print("main:",a,b,c)      # c 변수는 func3() 함수에서만 사용가능  error
print("main:",a,b)         # main: 100 200
func4()                    # func4() 함수 호출: 110 220
print("main:",a,b)         #  main: 100 200
func5()                    # func5() 함수 호출: 110 220
print("main:",a,b)         # main: 110 220


###------------

#매개변수
def add1(v1,v2):
    return v1+v2
def sub1(v1,v2):
    return v1-v2

hap = add1(10,20)   # 30
sub = sub1(10,20)     # -10
print(hap)
print(sub)

hap = add1(10.5,20.1)
sub = sub1(10.5,20.1)
print(hap)          # 30.6
print(sub)          # -9.600000000000001


###--------
#가변 매개 변수 : 매개변수의 갯수를 정하지 않음 경우
def multiparam(* p) :
    result = 0
    for i in p :
        result += i
    return result
print(multiparam())    # 0
print(multiparam(10))  # 10
print(multiparam(10,20))    # 30
print(multiparam(10,20,30)) # 60
print(multiparam(1.5,2.5,3)) #7.0
print(multiparam("1.5",2.5,3))  #result += i error


###---
# 딕셔너리 가변인자 **kwargs

def dictDefine(**kwargs):
    print('='*30)
    print(kwargs)
#     kwargs.sort() 에러
    for k in kwargs:
        print(k,':', kwargs[k])
    print('\n딕셔너리의 총 길이는?', len(kwargs))
# 함수 호출
dictDefine()
dictDefine(a='apple', b='banan', c='carrot')
dictDefine(n='nano', u='umbrella', m='moutain', s='sweet', d='dress')


###---
#매개변수에 기본값 설정
def hap1(num1=0,num2=1) :  #매개변수가 없는 경우 0,1 기본값 설정됨
    return num1+num2

print(hap1())    #num1=0,num2=1 기본값 설정
print(hap1(10))  #num1=10,num2=1 기본값 설정
print(hap1(10,20)) #num1=10,num2=20
print(hap1(0,20))  #num1=0,num2=20

###---
# 람다식을 이용한 함수
hap2=lambda num1,num2:num1+num2  
#print(hap2(10))  #오류 
print(hap2(10,20))  #30
print(hap2(10.5,20.5)) #31.0

#기본값 매개변수
hap3=lambda num1=0,num2=1:num1+num2
print(hap3(10))  #11
print(hap3(10,20))  #30
print(hap3(10.5,20.5)) #31.0

###람다를 함수를 이용한 map
mylist = [1,2,3,4,5]
add = lambda num:num+10
mylist = list(map(add,mylist))
print(mylist)    #[11, 12, 13, 14, 15]
#num : mylist의 요소값 한개.
mylist = list(map(lambda num:num-10,mylist))
print(mylist) #[1,2,3,4,5]
mylist = list(map(lambda num:num*10,mylist))
print(mylist)  # [10, 20, 30, 40, 50]

###----
# 복수 리스트에 적용하는 람다함수

list1=[1,2,3,4]
list2=[10,20,30,40]
list3=[10, 20, 30, 40, 50]
hap=lambda n1,n2:n1+n2
haplist=list(map(hap,list1,list2))
print(haplist)   #[11, 22, 33, 44]

haplist = list1 + list2 + list3 
# [1, 2, 3, 4, 10, 20, 30, 40, 10, 20, 30, 40, 50]

# 리스트 중 최소요소갯수의 리스트의 갯수로 맞춤.
list1.append(0)
list2.append(0)
haplist = list(map(lambda n1,n2,n3:n1+n2+n3,list1,list2, list3))
print(haplist)   #[21, 42, 63, 84, 50] 