def gugudan(n):
    print(n,"단을 출력합니다.")
    for i in range(1,9+1):
        print(n, "x", i, "=", n*i)

if __name__ == '__main__': #자기모듈이면 3단이 실행되고 다른모듈에서 임포트 하면 실행 안됨 
    gugudan(3)