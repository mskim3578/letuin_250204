#파일 쓰기 :콘솔에 내용을 입력 받아 파일로  저장 하기
#현재 폴더에 data/data.txt에 저장한다

outfp = open ("data/data.txt", "w", encoding="UTF-8")
while True :
    outstr = input("내용입력 =>")
    if outstr == '':
       break
        
    outfp.writelines(outstr+"\n")
outfp.close()   #!!! close를 해야 저장을 확인 할수 있다 



'''
  readline() : 한줄씩 읽기
  read()     : 버퍼의 크기만큼 한번 읽기
  readlines() : 한줄씩 한번에 읽어서 줄별로 리스트로 리턴
'''

# data.txt 파일을 읽어서 화면에 출력하기
infp = open("data/data.txt","r",encoding="UTF-8")

while True :
    instr = infp.readline() #한줄씩 읽기
    if instr == None or instr == "" :
        break
    print(instr,end="")
infp.close()    

infp = open("data/data.txt","r",encoding="UTF-8")
print(infp.read())
infp.close()

infp = open("data/data.txt","r",encoding="UTF-8")
print(infp.readlines())
infp.close()


#이미지 파일 읽어 복사하기
#apple.gif 파일을 읽어서 apple2.gif로 복사하기

infp = open("data/apple.gif", "rb" )
outfp = open("data/apple2.gif", "wb")

while True:
    indata = infp.read()
    if not indata : #파일의 끝 EOF(End of File)
       break 
    outfp.write(indata)
infp.close()
outfp.close()




   
import os
#현재 작업 폴더 위치 조회
print(os.getcwd())    
#작업 폴더의 위치 변경
os.chdir("c:/Users/admin")
print(os.getcwd())   

os.chdir("c:/workspace")
print(os.listdir())   
#파일의 정보 조회

# 폴더만 가능함 파일은 확인 하지 못함
file = os.getcwd()
file
if os.path.isfile(file) :
    print(file,"은 파일입니다.")
elif os.path.isdir(file) :    
    print(file,"은 폴더입니다.")

if os.path.exists(file) :    
    print(file,"은 존재합니다.")
else :    
    print(file,"은 없습니다.")


#현재 작업폴더
cwd = os.getcwd();
cwd
for f in os.listdir() :
    if os.path.isfile(f) :
        print(f,":파일, 크기:",os.path.getsize(f))
    elif os.path.isdir(f) :
        os.chdir(f)
        print(f,":폴더, 하위파일의갯수:",len(os.listdir()))
        os.chdir(cwd)

print(os.getcwd()) 
#폴더 생성
os.mkdir("temp") #temp 폴더 생성
#폴더 제거
os.rmdir("temp") #temp 폴더 제거



#######엑셀 파일 읽기
import openpyxl 
'''
   pip install openpyxl
   
   xlsx : openpyxl  모듈사용
   xls  : xlrd 모듈로 읽기
          xlwd 모듈로 쓰기
'''

filename = "data/sales_2015.xlsx"
#엑셀파일 전체 
book = openpyxl.load_workbook(filename)
# 첫번째 sheet
sheet = book.worksheets[0]


data=[]
for row in sheet.rows :
    row.index
    line = []
    #print(row)
    #enumerate(row) : 목록에서 
    #                 l : 인덱스
    #                 d : 데이터. 셀의값
    enumerate(row)
    for i,d in enumerate(row) :       
        line.append(d.value) #셀의내용을 line 추가
#    print(line) #한 줄의 셀의 리스트
    data.append(line)
print(data)

