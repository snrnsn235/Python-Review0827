# 점수받아 학점출력

while True :

    score =int(input("값 입력 : "))
    if (score <0 or score >100) : continue
    
    if score >=90:
        print("A", end=" ")
    elif score >=80:
        print("B", end=" ")
    elif score >=70:
        print("C.", end=" ")
    elif score >=60:
        print("D", end=" ")
    else :
        print("학고!!", end=" ")


    print("학점입니다. -.-")
