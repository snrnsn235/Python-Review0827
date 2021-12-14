print()
##딕셔너리
#리스트의 인덱스 대신 키 사용 딕셔너리는 키를 이용하여 값을 찾아낼 때 편리
#딕셔너리는 리스트와 달리 값의 순서를 지켜주지 않는다.
#리스트는 대괄호 튜플은 소괄호 딕셔너리는 중괄호{}로 집합을 만든다.

#학생 정보의 리스트 표현
student1=[1000,'홍길동', '컴공']
print(student1[1])

student1.append('010-3660-0658')
print(student1[3])

del(student1[0]) #리스트에서 해당 위치의 항목을 삭제한다.
print(student1)

student1.pop()
print(student1)

student1.clear()
print(student1)

print()



print()
#학생 정보의 딕셔너리 표현
student={'학번':1000,'이름':'이재협','전공':'언어청각치료학과'}
print(student['이름'])
#print(student[1])key에러발생
print(student['학번'])
print(student['전공'])
print()
#딕셔너리에 값 추가, 새로운 키에 값 대입, 마지막에 추가
student['연락처']='010-3660-0658'
print(student)
#student.append('010-3660-0658') #딕셔너리는 remove(), append()함수를 적용할수없다.
del(student['학번']) #리스트에서 해당 위치의 항목을 삭제한다.
print(student)
student.pop('전공')
print(student)
print()
#딕셔너리와 리스트의 공통점
student.clear() #clear() 함수를 사용하면 딕셔너리와 리스트의 내용이 모두 지워짐
print(student)


singer={}

singer['이름'] = '아이오아이'
singer['구성원수'] = 11
singer['데뷰'] = '프로듀스101'
singer['대표곡'] = '픽미픽미픽미업'

for i in singer.keys():
    print('%s-->%s' %(i, singer[i]))









