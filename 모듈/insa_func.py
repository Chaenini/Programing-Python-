#141
from 모듈 import greeting_func, hello_func


def main():
    print("insa_func 모듈입니다.")
    print("__name__ : ",__name__)
    #__name__ : 자기 실행문은 __main__으로 출력
    #__name__ : 자기 실행문이 아니면 자기 이름으로 출력
    hello_func.hello()
    greeting_func.greeting()

main()