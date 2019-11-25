from choice import Choice
from schoolFileReader import SchoolFileReader

while True :
    print("이용하고 싶은 서비스를 입력해주세요 : ")
    print("1. 관심있는 분야의 고등학교 알아보기\n2. 마이페이지")

    write = input()

    if write == "1":
        c = Choice()
        c.choice()

        while True:
            print("다시 시작하시겠습니까 ?(y / n) ")
            answer = input()

            if answer == "y":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n다시 시작합니다 ! ")
                break
            elif answer == "n":
                print("종료합니다 ! ")
                break
            else:
                print("다시 입력 해주세요")

    elif write == "2" :
        fr = SchoolFileReader()
        fr.schoolFileReader()

        while True:
            print("다시 시작하시겠습니까 ?(y / n) ")
            answer = input()

            if answer == "y":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n다시 시작합니다 ! \n")
                break
            elif answer == "n":
                print("종료합니다 ! ")
                break
            else:
                print("다시 입력 해주세요")

    if answer == "n" :
        break