print("학번을 입력하세요")
num = input()

grade = num[0:1]
number = num[1:2]

if grade == "1" or grade == "2":
    if number == "1" or number == "2" :
        print("뉴미디어 소프트웨어과")
    elif number == "3" or number == "4" :
        print("뉴미디어 웹솔루션과")
    elif number == "5" or number == "6" :
        print("뉴미디어 디자인과")
elif grade == "3" :
    if number == "1" or number == "2" :
        print("인터렉티브 미디어과")
    elif number == "3" or number == "4" :
        print("뉴미디어 디자인과")
    elif number == "5" or number == "6" :
        print("뉴미디어 솔루션과")
else : 
    print("잘못입력")