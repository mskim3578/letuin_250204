
###---  정수형 리스트
a=[0,0,0,0] #[10,20,30,40]
b=[]
print(a,len(a))      #len(a) : 리스트 요소의 갯수
print(b,len(b))

#a 리스트의 길이 만큼 숫자를 입력받아, a에 저장하고, 입력받은 수의
# 전체 합계를 출력하기
# for 문만 먼져실행행
hap=0
for i in range(len(a)) :#i: 0 ~ 3
    a[i] = int(input(str(i+1)+'번째 숫자 입력: '))
    hap += a[i]
print(a,"요소의 합:",hap) 
print(a,"요소의 합:",sum(a))  
#sum(리스트) : 리스트요소의합   

 # %s : 문자열을 지정하는 형식지정문자
#pop : LIFO(stack) 관련 함수.  
#sort : 정렬 함수.

mylist = [30,10,20]
print("리스트:%s" % mylist)  # 리스트:[30, 10, 20]
mylist.append(40)
print("mylist.append(40) 리스트:%s" % mylist) # mylist.append(40) 리스트:[30, 10, 20, 40]
print("pop() 메서드 결과:%s" % mylist.pop())  #pop() 메서드 결과:40
print("pop() 메서드 후 리스트 :%s" % mylist)   # pop() 메서드 후 리스트 :[30, 10, 20]
mylist.sort()
print("mylist.sort() 후 리스트 : %s" % mylist)   # mylist.sort() 후 리스트 : [10, 20, 30]
mylist.reverse() #역순 재배치
print("mylist.reverse() 후 리스트 : %s" % mylist) # mylist.reverse() 후 리스트 : [30, 20, 10]



###----list 주요 함수2
print(mylist)  # [30, 20, 10]
print("20값의 위치: %d" % mylist.index(20))  # 20값의 위치: 1
mylist.insert(2,222)
print("mylist.insert(2,222) 후 리스트:%s"%mylist) # mylist.insert(2,222) 후 리스트:[30, 20, 222, 10]
mylist.remove(222)
print("mylist.remove(222) 후 리스트:%s"%mylist)  # mylist.remove(222) 후 리스트:[30, 20, 10]
mylist.extend([77,77,99])
print("mylist.extend([77,77,99]) 후 리스트:%s"%mylist)  # mylist.extend([77,77,99]) 후 리스트:[30, 20, 10, 77, 77, 99]
print("77값의 갯수:%s"%mylist.count(77)) # 77값의 갯수:2
#mylist의 요소중 200값이 없다. 실행오류 발생
print("200값의 위치: %d" % mylist.index(200)) #200값의 인덱스값 리턴
# ValueError: 200 is not in list --  문자열에는 있음 오류 발생
print("20값의 위치 : %d"% mylist.find(20)) 
# AttributeError: 'list' object has no attribute 'find'

###------튜플 사용하기
tp1=(10,20,30)
print(tp1)
#tp1.append(40)     #tuple은 변경 할 수 없음
list1 = list(tp1)   #tuple을 list로 변경 
list1.append(40)    #list 객체에 요소 추가 
tp1 = tuple(list1)  # list를 tuple로 변경
print(tp1)
print("tp1의 크기=",len(tp1))
print("tp[1:3]=",tp1[1:3])
print("tp[:3]=",tp1[:3])
print("tp[2:]=",tp1[2:])
print("tp[::2]=",tp1[::2])
print(tp1[0],tp1[1],tp1[2])    #인덱스를 이용하여 접근 가능
a,b,c,d=tp1                    #tuple의 각 요소를 각각의 변수에 저장
print(a,b,c,d)  

###------- 튜플 연산
my_tuple = (1, 2, 3)
my_list = [1,2,3]
my_list1 = [3,3]
print(my_tuple*3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(my_tuple + my_tuple)  # (1, 2, 3, 1, 2, 3)

### ----- 리스트 연산 (extend로 사용한다  )
print(my_list*2) # [1, 2, 3, 1, 2, 3] list도 가능하다 
print(my_list + my_list1)  # [1, 2, 3, 3, 3]

# Named Tuple => 반드시 1:1 대응!
student = (name, age, gender) = ('홍길동', 27, '남') 
# ('제인', 27, '여', True)의 경우 1:1이 아니라서 안 됨

print(f'학생 정보 = {student}', type(student))  # 학생 정보 = ('제인', 27, '여') <class 'tuple'>
print(f'이름 = {name}', type(name))   #  이름 = 제인 <class 'str'>
print(f'나이 = {age}', type(age))     #  나이 = 27 <class 'int'>
print(f'성별 = {gender}', type(gender))   #성별 = 여 <class 'str'>

###-----dictionary 객체들을 반복문으로 조회
score_dic = {'lee':100,'hong':70,'kim':90}

for n in score_dic :
    #n : key값
    print(n,"=",score_dic[n])



for n in score_dic.keys() :
    #n : key값
    print(n,"=",score_dic[n]) 
    
for n in score_dic.values() :
    #n : key값
    print(n,"=",score_dic[n]) 

for n,s in score_dic.items() :
    #n:키값
    #s:value값
    print(n,"=",s) #kim = 90
    
    

###------------집합 구현하기
set0 = set([1,2,3])
set0

set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,1,2,3,4,5}
print(set1)
print(set2)
set3 = {5,6,7,8}
#교집합 : 두개의 집합에 공통 요소들
print("set1과 set2의 교집합 요소:",set1 & set2)
print("set1과 set3의 교집합 요소:",set1 & set3)
print("set1과 set3의 교집합 요소:",set1.intersection(set3)) #교집합 함수 
#합집합 : 두개의 집합에 속한 모든 요소들
print("set1과 set2의 합집합 요소:",set1 | set2)
print("set1과 set3의 합집합 요소:",set1 | set3)
print("set1과 set3의 교집합 요소:",set1.union(set3))


### list Comprehension

numbers=[]
for n in range(1,11) : #1~10
    numbers.append(n)
print(numbers)

#컴프리헨션 이용
print(x for x in range(1,11))
clist=[x for x in range(1,11)]
print(clist)

###--------------Set Comprehension
#1 ~10사이의 짝수 제곱값을 가진 set 객체 생성하기
sets=set()
for n in range(2,11,2) : #1~10
    sets.add(n*n)
print(sets)

sets = {x*x for x in range(1,11) if x%2==0}
print(sets)

set1 = {x*x for x in range(2,11,2)}
print(sets)
print(sorted(sets, reverse=True)) #리스트

# 중첩 Comprehention
#2의 배수이고, 3의 배수인 값만 리스트에 추가하기.
list21=[x for x in range(1,11) if x%2==0 and x%3==0]
print(list21)
list21=[x for x in range(1,11) if x%2==0 if x%3==0]
print(list21)



#  중첩 사용 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)


# 컴프리헨션 표현식을 사용하지 않음
list1= []
for row in matrix:
    for x in row :
        list1.append(x) 
print(list1)

# row : [1,2,3]
# x : 1
list1 = [x for row in matrix for x in row]
print(list1)


##---------  map 함수 적용
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
# map() 사용
result = map(square, numbers)
print(result)  
#<map object at 0x0000018DF3C2A410>
print(list(result))   #[1, 4, 9, 16, 25]
# 결과 확인 (map 객체를 리스트로 변환)


