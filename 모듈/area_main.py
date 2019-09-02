from 모듈 import area2

area2.print_area(30, 20)
area2.print_area(40, 30)

for i in range(11,15):
    area2.print_area(i, 20)

    print("가로 : 30 세로 : 10","       삼각형의 넓이 : ", area2.box_area(width, height))
    print(area2.__name__)