print("학번을 입력하세요")
num = input()

if num[0:1] == "1" or num[0:1] == "2":
    if num[1:2] == "1" or num[1:2] == "2" :
        print("뉴미디어 소프트웨어과")
    elif num[1:2] == "3" or num[1:2] == "4" :
        print("뉴미디어 웹솔루션과")
    elif num[1:2] == "5" or num[1:2] == "6" :
        print("뉴미디어 디자인과")
elif num[0:1] == "3" :
    if num[1:2] == "1" or num[1:2] == "2" :
        print("인터렉티브 미디어과")
    elif num[1:2] == "3" or num[1:2] == "4" :
        print("뉴미디어 디자인과")
    elif num[1:2] == "5" or num[1:2] == "6" :
        print("뉴미디어 솔루션과")
else : 
    print("잘못입력")