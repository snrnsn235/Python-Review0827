print("QUIZ")
score= int()
while True:
    score=int(input("성적을 입력하세요(1~100) : "))
    if (score<0 or score >100) : continue
          
    if 95<= score <101:
        print("A+")
    elif score >= 90:
        print("A")
    elif score >= 85:
        print("B+")
    elif score >= 80:
        print("B")
    elif score >= 75:
        print("C+")
    elif score >= 70:
        print("C")
    elif score >= 65:
        print("D+")
    elif score >= 60:
        print("D")
    else :
        print("F")
    




