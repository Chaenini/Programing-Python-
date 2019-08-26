import plusGame
import lottoGame

def game() : 
    print("어서오세요! 챌겜입니다 :)")
    name = input("이름을 입력해주세요 : ")
    answer = input(name+"님 원하시는 게임을 선택해주세요 (1. 플러스게임 / 2. 로또게임) : ")

    if(answer == "1") :
        plusGame.plusnum()
    elif(answer == "2"):
        lottoGame.lotto()
    
    again()
            
def again():
    again = input("\n게임을 다시 하시겠습니까? (1:네 2:아니오) :")
    if again == "1" : 
        game()
    else : 
        print("종료합니다")