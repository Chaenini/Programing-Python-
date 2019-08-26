majors= [["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"], #0
        ["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"], #1
        ["인터랙티브미디어과","뉴미디어디자인과","뉴미디어솔루션과"]] #2

student_number = input("힉번을 입력하세요 : ")

grade= int(student_number[0])
classroom= int(student_number[1])
print(majors[grade-1][(classroom-1)//2])
#[grade-1] = 리스트 칸 정하기 1학년이면 0번째 2학년이면 1번째 3학년이면 2번째 
#[(classroom-1)//2] = 리스트 안에 자리 정하기 1,2반이면 0, 3,4반이면 1 , 5,6반이면 2