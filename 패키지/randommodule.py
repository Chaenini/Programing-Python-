import random

print("0이상 1미만 실수 값 ")
print("ramdon.random() : ",random.random())
print()
print("시작값 2.5이상 끝값 10.0 미만 실수 값 ")
print("random.uniform(2.5,10.0) : ",random.uniform(2.5,10.0))
print()
print("0이상 끝값 10 미만 정수 값")
print("random.randrange(10) : ",random.randrange(10))
print()
print("1 이상 끝값 7 미만, 증가 값이 2인 정수 값")
print("random.randrange(1, 7, 2) : ",random.randrange(1, 7, 2))
# = random.randrangae(1,7+1)
#끝값이들어가는지 안들어가는지 차이
print()
print("1이상 끝값 7이하, 정수값")
print("random.randint(1,7) : ",random.randint(1,7))
print()
print("리스트에서 1개 값 꺼내오기")
season = ["봄","여름","가을","겨울"]
print("season : ",season)
print("random.choice(season) : ",random.choice(season))
print()
l = ["가","나","다","라","마"]
print("리스트 순서 섞기")
print("섞기 전 l : ",l)
print("random.shuffle(l) : ",random.shuffle(l))
print("섞은 후 l : ",l)
print()
print("리스트에서 몇개의 값을 중복하지 않고 3개 뽑기")
sample = ["1반","2반","3반","4반","5반","6반"]
print("샘플 대상 : ",sample)
print("random.sample(sample,3) : ",random.sample(sample,3))
