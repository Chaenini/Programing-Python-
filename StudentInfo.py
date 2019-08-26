majors= [
        ["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
        ["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
        ["인터랙티브미디어과","뉴미디어디자인과","뉴미디어솔루션과"]
        ]

student_number = input("학번을 입력하세요 : ")

grade= int(student_number[0])
classroom= int(student_number[1])

print(student_number[0]+"학년",majors[grade-1][c(lassroom-1)//2],student_number[1]+"반",student_number[2:]+"번 입니다.")
# 반
# 1,2  -1=> 0, 1 => 0
# 3,4  -1=> 2,3 => 1
# 5,6  -1=> 4,5 => 2 