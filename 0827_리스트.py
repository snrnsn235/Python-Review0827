#파이썬, 이재협, 0827
###리스트, 딕셔너리, 튜플

#리스트
#4개의 값을 입력받아 더하는 프로그램 작성

a, b, c, d = 0, 0, 0, 0
hap=0

a=int(input("1번째 숫자 : "))
b=int(input("2번째 숫자 : "))
c=int(input("3번째 숫자 : "))
d=int(input("4번째 숫자 : "))

hap=a+b+c+d

print("합계 ==> %d " %hap)
'''
#리스트의 인덱스 0~3까지 입력받은 값 저장
'''
print()
aa=[0,0,0,0]
hap=0

aa[0]=int(input("1번째 숫자 : "))
aa[1]=int(input("2번째 숫자 : "))
aa[2]=int(input("3번째 숫자 : "))
aa[3]=int(input("4번째 숫자 : "))

hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계 ==> %d" %hap) #%d = %hap
'''
#리스트와 반복문 for의 활용
'''
print()
hap=0
aa=[0,0,0,0]

for i in range(0, 4, 1):
    aa[i] = int(input(str(i+1)+"번째 숫자 : ")) #숫자와 문자열은 + 연산불가, str함수사용
    hap+=aa[i]

print("합계 ==> %d" %hap) #%d = %hap
'''
#융동성있게 확장할 수 있도록 빈 리스트 생성
'''
aa=[]
print(aa)
aa.append(0)
print(aa)
aa.append(0)
print(aa)
print()
aa=[]
hap=0

for i in range(0,4,1): #초기값=0, 증가값-1 생
    aa.append(0)
    aa[i] = int(input(str(i+1)+"번째 숫자 : "))
    hap+=aa[i]
print("합계 ==> %d" %hap) #%d = %hap
print()

aa=[]
hap=0

for i in range(0,10,1): #초기값=0, 증가값-1 생
    aa.append(0)
    aa[i] = int(input(str(i+1)+"번째 숫자 : "))
    hap+=aa[i]
print("합계 ==> %d" %hap) #%d = %hap
print()

aa=[]
hap=0

for i in range(0,4,1): #초기값=0, 증가값-1 생
    aa.append(0)
    aa[i] = int(input(str(i+1)+"번째 숫자 : "))
    print(aa[i])
    hap+=aa[i]
print("합계 ==> %d" %hap) #%d = %hap
print(aa)
print(aa[0:3])
'''

#리스트 조작 함수 사용
'''
myList = [30, 10, 20]
print(myList)

myList.append(40) #리스트 제일 뒤에 항목 추가
print(myList)

myList.pop() #리스트 제일뒤의 항목을 빼내고, 빼낸 항목은 삭제한다.
print(myList)

myList.sort() #리스트의 항목을 정렬한다.
print(myList)

myList.reverse() # 리스트 항목의 순서를 역순으로 만듦
print(myList)

print(myList.index(20)) #지정한 값을 찾아서 그 위치를 반환한다.
print(myList.index(30))
print(myList.index(10))

myList.insert(2, 222) #지정된 위치에 값을 삽입한다.
print(myList)

myList.remove(222) #리스트에서 지정한 값을 제거한다. 단 여러 개일 경우 첫번째 값만 지운다
print(myList)

myList.extend([77, 88, 77])#리스트 뒤에 추가, 리스트의 더하기 연산과 동일한 기능을 한다.
print(myList)

print(myList.count(77))#리스트에서 찾을 값의 개수를 센다

del(myList[0]) #리스트에서 해당 위치의 항목을 삭제한다.
print(myList)

print(len(myList)) #리스트에 포함된 전체 항목의 개수를 센다.
print()
#2차원 리스트

list1=[] #빈 리스트 작성
list2=[] #빈 리스트 작성
value=0 #리스트에 들어갈 값을 입력

#2차원 리스트 
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]
#2차원 리스트 출력
for i in range(0,3):
    for k in range(0,4):
        print("%3d" %list2[i][k], end=" ") #end=" "가로로 출력시키기 위해"
    print("")













































    
