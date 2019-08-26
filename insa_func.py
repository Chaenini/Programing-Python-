#141
import hello_func
import greeting_func

def main():
    print("insa_func 모듈입니다.")
    print("__name__ : ",__name__)
    #__name__ : 자기 실행문은 __main__으로 출력
    #__name__ : 자기 실행문이 아니면 자기 이름으로 출력
    hello_func.hello()
    greeting_func.greeting()

main()