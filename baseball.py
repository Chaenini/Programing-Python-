# 로또 게임
# 다섯자리 중복 없는 임의의 번호 생성 
# 무한 반복
# 사용자 입력 받기
# seaterr= 자릿수 틀림 / numerr = 숫자 틀림 판단
# 사용자 입력, seaterr, numerr 출력
# 임의의 수, 사용자 입력이 같으면 당첨, break if

import random

l = random.sample(range(1, 9+1), 3)
lotto = ''.join(str(i) for i in l[:3])
print(lotto)

while True :
  gamer = input("로또 번호를 맞춰주세요 ! (로또 번호는 !~10 사이 세개의 숫자입니다): ")
  gamer = gamer.replace(" ","")
  print(gamer)

  seatok = 0
  numerr = 0

  for i in range (len(lotto)) :
    for j in range (len(gamer)) : 
      if lotto[i] == gamer[j] : 
        if i == j :
          seatok += 1
        else :
          numerr += 1

  if lotto == gamer : 
    print("로또에 당첨 되셨습니다!")
    break
  else :
    print("입력하신 번호 : {}\n자리와 숫자 모두 맞은 수 : {}\n숫자는 맞고 자리는 틀린 수 : {}".format(gamer, seatok, numerr))
