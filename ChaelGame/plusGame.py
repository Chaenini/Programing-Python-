import os
import random 
import time

def plusnum():
    print("플러스 게임 입니다 ! 제시되는 숫자의 합을 구해주세요 ! (숫자는 5개 입니다.)")
    start = input("준비 되셨다면 완료 라고 입력하세요 >> ") 
    
    #게임 시작 
    if start == "완료":
        print("시작합니다 눈 크게 뜨세요 !")
        sum = 0
        os.system('cls')
        
        #5개의 랜덤 숫자를 0.5초 간격으로 보여주고 sum에 더하기 
        for num in range(1,6,1) :
            print("     ")
            n = random.randint(1,10)
            print(n)
            sum += n
            time.sleep(1/2)
            os.system('cls')
        
        # 사용자가 더한수를 맞출때까지 실행 
        while True :
            answer = input("합을 입력해주세요 ! ")
            
            if sum==int(answer) : 
                print("정답입니다 :)")
                break
            else : 
                print("오답입니다 :(")