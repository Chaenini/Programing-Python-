class car :
    count = 0 # car.count 라 쓰면 안됨 

    def __init__(self,type,speed):
        self.type = type
        self.speed = speed
        car.count += 1 # count 만 쓰면 안됨 

    @classmethod #반드시 있어야함
    def get_count(cls) : # 꼭 cls 아니여도 됨 
        return cls.count #car.count 라고 써도 됨 

    def move(self) : 
        print(self.type+"가 "+str(self.speed)+"속도로 움직입니다.")

    def speed_up(self,amount) : 
        self.speed += amount # 그냥 speed 쓰면 안됨 
    
    def speed_down(self, amount) :
        self.speed -= amount 

print(car.get_count())

c = car("스포츠카",200)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move()

d = car("테슬라",200)
d.speed_up(50)
d.move()
d.speed_down(150)
d.move()

print(car.get_count())